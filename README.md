


# 🤖 Emotion Detector & Smart Chatbot

This project is an interactive AI chatbot that detects a user's emotion via webcam using facial expression analysis and responds with personalized replies and mood-lifting quotes. Built using **Streamlit**, **DeepFace**, and **OpenCV**, it’s designed to simulate an emotionally aware chat interface — ideal for mental wellness and intelligent user interaction demos.

---

## 🚀 Features

- 🎥 Real-time webcam preview before emotion detection  
- 😄 Detects emotions using DeepFace (Happy, Sad, Angry, Fear, Disgust, Surprise, Neutral)  
- 💬 Emotion-aware chatbot response system  
- 💡 Motivational quote generator based on detected emotion  
- 🖥️ Interactive Streamlit web interface

---

## 🛠️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ranjanihub/emotional-chatbot.git
   cd emotion-chatbot


2. **Create a Virtual Environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🧠 Requirements

Make sure you have the following installed:

* Python 3.8 or higher
* Webcam-enabled device
* `pip` (Python package manager)

### Required Python Libraries:


streamlit
opencv-python
deepface
numpy
pillow


Create a `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

---

## 🧪 Running the App

To launch the app in your local browser:

```bash
streamlit run emotion_chatbot.py
```

---

## 📁 Project Structure

```text
emotion-chatbot/
│
├── emotion_chatbot.py        # Main Streamlit app
├── requirements.txt          # Required Python packages
└── README.md                 #
```
