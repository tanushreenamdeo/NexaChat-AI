# 🤖 NexaChat AI – Simple AI Chatbot

NexaChat AI is a web-based chatbot developed using Streamlit and Groq API. It allows users to interact with an AI model through text and voice input while maintaining chat history across multiple sessions. The application is simple, user-friendly, and accessible from both mobile and desktop devices.

---

## 🚀 Features

- 💬 AI chatbot using Groq (LLaMA 3.1 model)
- 🧠 Multiple chat sessions (like ChatGPT)
- 📝 Automatic chat title generation
- 📂 Chat history displayed in sidebar (Recent Chats)
- 🎤 Voice input (speech-to-text)
- 🔊 Voice output (text-to-speech)
- 🌐 Accessible on mobile and desktop browsers

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Groq API  
- SpeechRecognition  
- gTTS (Google Text-to-Speech)  

---

## 📁 Project Structure
# 🤖 NexaChat AI – Simple AI Chatbot

NexaChat AI is a web-based chatbot developed using Streamlit and Groq API. It allows users to interact with an AI model through text and voice input while maintaining chat history across multiple sessions. The application is simple, user-friendly, and accessible from both mobile and desktop devices.

---

## 🚀 Features

- 💬 AI chatbot using Groq (LLaMA 3.1 model)
- 🧠 Multiple chat sessions (like ChatGPT)
- 📝 Automatic chat title generation
- 📂 Chat history displayed in sidebar (Recent Chats)
- 🎤 Voice input (speech-to-text)
- 🔊 Voice output (text-to-speech)
- 🌐 Accessible on mobile and desktop browsers

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Groq API  
- SpeechRecognition  
- gTTS (Google Text-to-Speech)  

---

## 📁 Project Structure
nexachat.ai/
app.py
requirements.txt
 
 
Create virtual environment:

python -m venv venv
venv\Scripts\activate


3. Install dependencies:

pip install -r requirements.txt


4. Add API Key:  
Create a `.env` file in your project folder and add:

GROQ_API_KEY=your_api_key_here


---

## ▶️ Run the Application


streamlit run app.py


---

## 🌐 Deployment

This project is deployed using Streamlit Cloud and hosted through GitHub.  
After deployment, it can be accessed using a public link from any device.

Example:

https://nexachat-ai.streamlit.app


---

## 📱 Accessibility

The chatbot works on:
- Desktop browsers  
- Android devices  
- iOS devices  

---

## ⚠️ Important Notes

- Do not upload your `.env` file to GitHub as it contains sensitive API keys.
- Voice input may not work in deployed version due to browser limitations.
- Ensure proper internet connection for API responses.

---

## 🧠 Project Description

This project demonstrates the development of a conversational AI chatbot using modern APIs. It focuses on real-time interaction, session-based chat history, and deployment of AI applications on cloud platforms.

---

## 👩‍💻 Author

Tanushree Namdeo

---

## 📌 Future Improvements

- Add user authentication (login/signup)
- Improve UI with animations
- Add file upload (PDF-based chat)
- Enhance chatbot response accuracy
