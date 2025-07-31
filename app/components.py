import streamlit as st

def emotion_feedback_card(emotion: str, response: str):
    color_map = {
        "happy": "#D4EDDA",
        "sad": "#F8D7DA",
        "angry": "#F8D7DA",
        "neutral": "#FFF3CD",
        "surprise": "#D1ECF1",
        "fear": "#D1ECF1",
        "disgust": "#F0E68C"
    }

    emoji_map = {
        "happy": "😊",
        "sad": "😢",
        "angry": "😠",
        "neutral": "😐",
        "surprise": "😲",
        "fear": "😨",
        "disgust": "🤢"
    }

    emotion = emotion.lower()

    # Emotion card
    st.markdown(f"""
        <div style="background-color:{color_map.get(emotion, '#F0F0F0')}; padding:20px; border-radius:15px; margin-top:20px;">
            <h2 style="text-align:center;">{emoji_map.get(emotion, '💬')} {emotion.capitalize()}</h2>
            <p style="text-align:center; font-size:18px;">{response}</p>
        </div>
    """, unsafe_allow_html=True)

    # Add calming animation for negative emotions
    if emotion in ["sad", "angry"]:
        st.markdown("""
            <div style="text-align:center; margin-top:20px;">
                <img src="https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif" width="250"/>
                <p><em>Take a deep breath. Inhale... Exhale...</em></p>
            </div>
        """, unsafe_allow_html=True)
