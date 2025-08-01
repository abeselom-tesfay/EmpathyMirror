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

    gif_map = {
        "happy": "https://media.giphy.com/media/111ebonMs90YLu/giphy.gif",
        "sad": "https://media.giphy.com/media/d2lcHJTG5Tscg/giphy.gif",
        "angry": "https://media.giphy.com/media/l41YtZOb9EUABnuqA/giphy.gif",
        "neutral": "https://media.giphy.com/media/3oEduNCSvS1BJ0U8xe/giphy.gif",
        "surprise": "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
        "fear": "https://media.giphy.com/media/3o7qE1YN7aBOFPRw8E/giphy.gif",
        "disgust": "https://media.giphy.com/media/3oz8xPQ9pGU9q9Ph9K/giphy.gif",
    }

    emotion = emotion.lower()

    st.markdown(f"""
        <div style="background-color:{color_map.get(emotion, '#F0F0F0')}; 
                    padding:20px; border-radius:15px; margin-top:20px; text-align:center;">
            <div style="font-size:60px;">{emoji_map.get(emotion, '💬')}</div>
            <h2 style="margin-bottom:5px;">{emotion.capitalize()}</h2>
            <p style="font-size:18px; margin-top:0;">{response}</p>
            <img src="{gif_map.get(emotion)}" width="250" style="margin-top:15px;"/>
        </div>
    """, unsafe_allow_html=True)
