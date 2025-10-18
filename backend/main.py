# backend/main.py
from fastapi import FastAPI, File, UploadFile, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import tensorflow as tf
import numpy as np
import cv2
import base64
import io
from PIL import Image
import json
from datetime import datetime
import uuid

app = FastAPI(title="EmpathyMirror API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your trained model
model = tf.keras.models.load_model('model/face_emotion_model.keras')

# Emotion labels (adjust based on your FER2013 model)
EMOTIONS = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Empathetic responses mapping
EMPATHETIC_RESPONSES = {
    'Angry': [
        "I see you're feeling angry. It's okay to feel this way. Would you like to talk about what's bothering you?",
        "I sense your frustration. Sometimes taking a deep breath can help."
    ],
    'Happy': [
        "Your happiness is contagious! 😊 Keep shining!",
        "Seeing you smile brightens up the space! What's making you feel good?"
    ],
    'Sad': [
        "I notice you seem sad. Remember, it's okay to not be okay. I'm here for you.",
        "Your feelings are valid. Would a virtual hug help? *sends warm hug*"
    ],
    'Fear': [
        "I sense some fear. You're stronger than you think. You've got this!",
        "It's okay to feel scared. Remember to breathe deeply."
    ],
    'Surprise': [
        "Wow! Something surprised you! Hope it's a pleasant surprise!",
        "That expression! Something unexpected happened?"
    ],
    'Neutral': [
        "I see you're feeling calm and centered. Peaceful moments are precious.",
        "A moment of calm reflection. How are you truly feeling today?"
    ],
    'Disgust': [
        "I sense some discomfort. Sometimes stepping away can provide perspective.",
        "That doesn't seem pleasant. Want to share what's bothering you?"
    ]
}

def preprocess_image(image_data):
    """Preprocess image for model prediction"""
    # Decode base64 image
    if ',' in image_data:
        image_data = image_data.split(',')[1]
    
    image_bytes = base64.b64decode(image_data)
    image = Image.open(io.BytesIO(image_bytes))
    
    # Convert to grayscale and resize to 48x48 (FER2013 standard)
    image = image.convert('L')
    image = image.resize((48, 48))
    
    # Normalize pixel values
    image_array = np.array(image) / 255.0
    image_array = image_array.reshape(1, 48, 48, 1)
    
    return image_array

@app.post("/api/analyze-emotion")
async def analyze_emotion(image_data: dict):
    try:
        image_array = preprocess_image(image_data['image'])
        
        # Predict emotion
        predictions = model.predict(image_array)
        emotion_index = np.argmax(predictions[0])
        confidence = float(predictions[0][emotion_index])
        emotion = EMOTIONS[emotion_index]
        
        # Get empathetic response
        responses = EMPATHETIC_RESPONSES.get(emotion, ["I see how you're feeling."])
        empathetic_response = np.random.choice(responses)
        
        return JSONResponse({
            "emotion": emotion,
            "confidence": confidence,
            "empathetic_response": empathetic_response,
            "timestamp": datetime.now().isoformat(),
            "analysis_id": str(uuid.uuid4())
        })
        
    except Exception as e:
        return JSONResponse(
            {"error": f"Analysis failed: {str(e)}"},
            status_code=500
        )

@app.websocket("/ws/real-time-analysis")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            image_data = json.loads(data)
            
            image_array = preprocess_image(image_data['image'])
            predictions = model.predict(image_array)
            emotion_index = np.argmax(predictions[0])
            confidence = float(predictions[0][emotion_index])
            emotion = EMOTIONS[emotion_index]
            
            responses = EMPATHETIC_RESPONSES.get(emotion, ["I see how you're feeling."])
            empathetic_response = np.random.choice(responses)
            
            await websocket.send_json({
                "emotion": emotion,
                "confidence": confidence,
                "empathetic_response": empathetic_response,
                "timestamp": datetime.now().isoformat()
            })
            
    except Exception as e:
        await websocket.close(code=1011)

@app.get("/")
async def root():
    return {"message": "EmpathyMirror API - Advanced Facial Expression Recognition"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)