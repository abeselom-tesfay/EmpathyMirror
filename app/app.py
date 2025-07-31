import streamlit as st
import cv2
import numpy as np
from PIL import Image
from utils import load_model, preprocess_image, predict_emotion, EMOTION_RESPONSES

st.set_page_config(page_title="Empathy Mirror", layout="centered")

st.title("🪞 Empathy Mirror")
st.markdown("Upload an image or activate your camera to detect facial emotion in real-time.")

# Load the pre-trained model
model = load_model()

# Choose input method
input_method = st.radio("Choose input method:", ("Camera", "Upload Image"))

if input_method == "Upload Image":
    uploaded_file = st.file_uploader("Upload a facial image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image_np = np.array(image.convert("RGB"))  # Convert PIL to OpenCV format
        image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

        processed = preprocess_image(image_np)

        if processed is not None:
            emotion = predict_emotion(processed, model)
            st.image(image, caption=f"Detected Emotion: {emotion}", use_column_width=True)
            st.success(f"**{emotion}** - {EMOTION_RESPONSES[emotion.lower()]}")
        else:
            st.error("No face detected in the image.")

else:
    # Real-time webcam feed
    run = st.checkbox("Start Camera")
    FRAME_WINDOW = st.image([])

    camera = cv2.VideoCapture(0)

    while run:
        ret, frame = camera.read()
        if not ret:
            st.error("Failed to access webcam.")
            break

        processed = preprocess_image(frame)

        if processed is not None:
            emotion = predict_emotion(processed, model)
            label = f"{emotion}"
            response = EMOTION_RESPONSES[emotion.lower()]
            cv2.putText(frame, label, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
        else:
            response = "No face detected"

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)

    camera.release()
