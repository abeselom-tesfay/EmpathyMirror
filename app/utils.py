import streamlit as st
import cv2
import numpy as np
from keras.models import load_model as keras_load_model

@st.cache_resource
def load_model():
    return keras_load_model("model/emotion_model.h5")

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) == 0:
        return None

    (x, y, w, h) = faces[0]
    roi_gray = gray[y:y + h, x:x + w]
    roi_gray = cv2.resize(roi_gray, (48, 48))
    roi_gray = roi_gray.astype("float") / 255.0
    roi_gray = np.expand_dims(roi_gray, axis=-1)
    roi_gray = np.expand_dims(roi_gray, axis=0)
    return roi_gray

def predict_emotion(face_img, model):
    predictions = model.predict(face_img)
    emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
    return emotion_labels[np.argmax(predictions)]

EMOTION_RESPONSES = {
    "angry": "😠 It's okay to feel angry. Take a deep breath.",
    "disgust": "🤢 Something feels off? Stay grounded and breathe.",
    "fear": "😨 It's natural to feel fear. You are not alone.",
    "happy": "😊 Keep smiling and spread the joy!",
    "neutral": "😐 Feeling balanced is good. Stay mindful.",
    "sad": "😢 It's okay to be sad. Take your time to heal.",
    "surprise": "😲 Unexpected things happen. Stay curious!"
}
