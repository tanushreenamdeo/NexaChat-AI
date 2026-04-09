import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
import json
import speech_recognition as sr
from gtts import gTTS
import tempfile

# -------------------------
# LOAD ENV
# -------------------------
load_dotenv()
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

CHAT_FILE = "chats.json"

# -------------------------
# LOAD & SAVE
# -------------------------
def load_chats():
    if os.path.exists(CHAT_FILE):
        with open(CHAT_FILE, "r") as f:
            return json.load(f)
    return {}

def save_chats(data):
    with open(CHAT_FILE, "w") as f:
        json.dump(data, f)

# -------------------------
# AUTO TITLE GENERATION
# -------------------------
def generate_chat_title(message):
    return message[:30] + "..." if len(message) > 30 else message

# -------------------------
# VOICE INPUT
# -------------------------
def get_voice_input():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.info("🎤 Listening...")
            audio = r.listen(source, timeout=5)
        return r.recognize_google(audio)
    except:
        return None

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="NexaChat AI", layout="wide")

# -------------------------
# UI STYLE
# -------------------------
st.markdown("""
<style>
section[data-testid="stSidebar"] {
    background-color: #f8f9fa;
}
section[data-testid="stSidebar"] * {
    color: black;
}
.active-chat {
    background-color: #dbeafe !important;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# SESSION INIT
# -------------------------
if "chats" not in st.session_state:
    st.session_state.chats = load_chats()

if "current_chat" not in st.session_state:
    st.session_state.current_chat = "Current Chat "
    st.session_state.chats["Current Chat "] = []

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.title("💬 NexaChat")

if st.sidebar.button("➕ New Chat", key="new_chat_btn"):
    new_chat = f"Chat {len(st.session_state.chats)+1}"
    st.session_state.current_chat = new_chat
    st.session_state.chats[new_chat] = []

st.sidebar.markdown("### Recent Chats")

for i, chat in enumerate(list(st.session_state.chats.keys())[::-1]):
    
    # Highlight active chat
    label = f"👉 {chat}" if chat == st.session_state.current_chat else chat

    if st.sidebar.button(label, key=f"chat_{i}"):
        st.session_state.current_chat = chat

# -------------------------
# MAIN CHAT
# -------------------------
st.title("🤖 NexaChat AI")

messages = st.session_state.chats[st.session_state.current_chat]

# Display chat
for msg in messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -------------------------
# INPUT + MIC
# -------------------------
col1, col2 = st.columns([8,1])

with col1:
    user_input = st.chat_input("Type your message...")

with col2:
    if st.button("🎤", key="mic_btn"):
        voice = get_voice_input()
        if voice:
            user_input = voice

# -------------------------
# PROCESS
# -------------------------
if user_input:

    # If first message → rename chat
    if len(messages) == 0:
        new_title = generate_chat_title(user_input)
        st.session_state.chats[new_title] = st.session_state.chats.pop(st.session_state.current_chat)
        st.session_state.current_chat = new_title
        messages = st.session_state.chats[new_title]

    # User message
    messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=messages
                )
                reply = response.choices[0].message.content
            except Exception as e:
                reply = f"Error: {str(e)}"

            st.write(reply)

            messages.append({
                "role": "assistant",
                "content": reply
            })

            # Voice output
            try:
                tts = gTTS(reply)
                tmp = tempfile.NamedTemporaryFile(delete=False)
                tts.save(tmp.name)
                st.audio(tmp.name)
            except:
                pass

# -------------------------
# SAVE
# -------------------------
save_chats(st.session_state.chats)
