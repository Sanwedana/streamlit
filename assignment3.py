import streamlit as st
from google import genai
import os 
from dotenv import load_dotenv

st.title("The MULTIVERSE OF CHATBOTS 🪐")

# SIDEBAR Setup
with st.sidebar:
    st.header("Portal Settings ⚙️")
    personality = st.selectbox("Who do you want to talk to?",[
        "An expert Hacker", "An angry Ravi Shastri", "A crazy Ronaldo fan", "Donald Trump"
    ])

# API Setup
load_dotenv()
client = genai.Client(api_key=os.getenv("API_KEY"))

# ==========================================
# TASK 1: Initialize the Memory Vault
# ==========================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================================
# TASK 2: Render the Chat History
# ==========================================
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==========================================
# TASK 3: Upgrade the Input UI 
# ==========================================
if user_message := st.chat_input("Say something..."):
    
    # TASK 4 (Part A): Save New User Message to Memory
    st.session_state.messages.append({"role": "user", "content": user_message})
    
    # Display the user's message instantly on screen
    with st.chat_message("user"):
        st.markdown(user_message)
        
    # Prepare instructions for the AI
    ai_instructions = (
        f"You are acting as {personality}. Respond to the message sent by the user "
        f"staying completely in character. User message: {user_message}"
    )
    
    with st.spinner("Connecting to the multiverse!......"):
        # Generate the response
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=ai_instructions
        )
        
        # TASK 4 (Part B): Save AI Response to Memory
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        
        # Display the AI's response on screen
        with st.chat_message("assistant"):
            st.markdown(response.text)