import streamlit as st
from deepface import DeepFace
import cv2
import numpy as np
from PIL import Image
import time

# Global variable to store detected emotion
if "user_emotion" not in st.session_state:
    st.session_state.user_emotion = "neutral"


# Emotion-based chatbot responses
def get_response(emotion, user_message):
    emotion = emotion.lower()

    responses = {
        "happy": f"I'm so glad to hear from you! 😊 {user_message}? That sounds exciting!",
        "sad": f"I'm here for you 😔. {user_message}? Tell me more so I can help.",
        "angry": f"I understand it's frustrating 😠. Let's try to work through this together.",
        "surprise": f"Whoa! 😲 {user_message}? That's unexpected!",
        "fear": f"It's okay to feel scared 😟. I'm here with you. Let’s take it slow.",
        "disgust": f"Yikes 😷. That doesn't sound good. Want to talk more about it?",
        "neutral": f"Thanks for your message! 🙂 How can I assist you further?"
    }

    return responses.get(emotion, "I'm here to help. Tell me more!")


# Mood-lifting quotes
mood_lifting_quotes = {
    "happy": "Keep shining! 🌟 Your smile lights up the world.",
    "sad": "Every storm runs out of rain. ☀️ Better days are coming!",
    "angry": "Breathe. Let go. And remind yourself that this too shall pass. 🌈",
    "surprise": "Life is full of surprises—embrace the magic! ✨",
    "fear": "You are stronger than your fears 💪. Keep moving forward.",
    "disgust": "Focus on the good—it’s always around you. 💚",
    "neutral": "Stay positive and curious! The best is yet to come. 🚀"
}


# Show webcam and detect emotion
def detect_emotion():
    cap = cv2.VideoCapture(0)
    detected_emotion = "neutral"
    stframe = st.empty()
    st.info("📸 Please look at the camera. Detecting emotion in 5 seconds...")

    start_time = time.time()
    while time.time() - start_time < 5:
        ret, frame = cap.read()
        if not ret:
            continue
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame_rgb, channels="RGB")

    # Final capture for emotion detection
    ret, frame = cap.read()
    cap.release()
    stframe.empty()

    if ret:
        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            detected_emotion = result[0]['dominant_emotion']
            st.success(f"🎯 Detected Emotion: **{detected_emotion.upper()}**")
            quote = mood_lifting_quotes.get(detected_emotion.lower(), "You're doing great! Keep going.")
            st.info(f"💡 Mood Boost: *{quote}*")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Failed to capture image.")
    return detected_emotion


# Streamlit App
def main():
    st.set_page_config(page_title="Emotion Chatbot", page_icon="💬")
    st.title("🤖 Emotion Detector & Smart Chatbot")

    if st.button("Start Emotion Detection"):
        emotion = detect_emotion()
        st.session_state.user_emotion = emotion

    if st.session_state.user_emotion:
        st.markdown(f"### Detected Emotion: **{st.session_state.user_emotion.upper()}**")
        st.markdown("### 💬 Start Chatting with the Bot")
        user_input = st.text_input("You:", key="user_input")

        if user_input:
            bot_reply = get_response(st.session_state.user_emotion, user_input)
            st.markdown(f"**Bot:** {bot_reply}")

    st.markdown("---")
    st.caption("Created for AI Expo 2025 🚀")


if __name__ == "__main__":
    main()
