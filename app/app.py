import streamlit as st
import cv2
import numpy as np
from PIL import Image
from utils import load_model, preprocess_image, predict_emotion, EMOTION_RESPONSES
from components import emotion_feedback_card

# Page config must be the first Streamlit command
st.set_page_config(page_title="Empathy Mirror", layout="wide")

# --- Custom CSS for layout ---
st.markdown("""
    <style>
    .app-container {
        max-width: 75vw;
        margin-left: auto;
        margin-right: auto;
    }
    .navbar {
        background-color: #4A90E2;
        padding: 15px;
        font-size: 28px;
        color: white;
        font-weight: bold;
        text-align: center;
        border-radius: 5px;
        margin-bottom: 20px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .touch-description {
        padding: 10px;
        background-color: #f9f9f9;
        border-radius: 10px;
        transition: background-color 0.3s ease;
        font-size: 16px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .touch-description:hover {
        background-color: #e6f0ff;
    }
    </style>
""", unsafe_allow_html=True)

# --- Begin content within custom container ---
st.markdown('<div class="app-container">', unsafe_allow_html=True)

# --- Navbar ---
st.markdown('<div class="navbar">Empathy Mirror</div>', unsafe_allow_html=True)

# --- Top 50/50 Layout: Left = Description, Right = Input Method + Upload/Camera Controls ---
col1, col2 = st.columns(2)

with col1:
    st.title("Empathy Mirror")
    st.markdown("### A human-centered AI experience")
    st.markdown("""
        <div class="touch-description">
        Reflecting your emotion with care and compassion. Explore how artificial intelligence can build trust and promote empathy through responsible interaction design.
        </div>
    """, unsafe_allow_html=True)

with col2:
    input_method = st.radio("Choose input method:", ("Camera", "Upload Image"))

    # Controls now inside the right column
    if input_method == "Upload Image":
        uploaded_file = st.file_uploader("Upload a facial image", type=["jpg", "jpeg", "png"])
    else:
        run = st.checkbox("Start Camera")

# --- Load model only once ---
model = load_model()

# --- Main Interaction Area ---
if input_method == "Upload Image" and uploaded_file:
    image = Image.open(uploaded_file)
    image_np = np.array(image.convert("RGB"))
    image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    processed = preprocess_image(image_np)

    if processed is not None:
        emotion = predict_emotion(processed, model)

        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(image, caption="Your Uploaded Image", use_column_width=True)
        with col2:
            emotion_feedback_card(emotion, EMOTION_RESPONSES[emotion.lower()])
    else:
        st.error("No face detected in the image.")

elif input_method == "Camera" and 'run' in locals() and run:
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)

    while run:
        ret, frame = camera.read()
        if not ret:
            st.error("Webcam access failed.")
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

# --- User Feedback ---
feedback = st.radio("Did this reflection feel helpful to you?", ["👍 Yes", "👎 Not really"], index=None)
if feedback:
    st.success("Thank you for your feedback 💙")

# --- HCI Context ---
with st.expander("Why Empathy Mirror?"):
    st.markdown("""
    *Empathy Mirror* is an emotionally-aware AI system that promotes thoughtful, responsible, and compassionate human-computer interaction.
    It recognizes the user’s emotional state and responds with non-judgmental and affirming feedback.

    This prototype aims to:
    - Build trust in AI  
    - Improve emotional awareness  
    - Demonstrate ethical interaction design in practice
    """)

# --- End container ---
st.markdown('</div>', unsafe_allow_html=True)
