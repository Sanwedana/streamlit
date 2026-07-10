import streamlit as st
from google import genai
import os 
from dotenv import load_dotenv

st.title("The MULTIVERSE OF CHATBOTS!!!")

with st.sidebar:
    st.header("Portal Settings.")
    personality = st.selectbox("Who do you want to talk to?",[
        "An expert Hacker", "An angry Ravi Shastri", "A crazy Ronaldo fan", "Donald Trump", "Custom Character..."
    ])
    
    if personality == "Custom Character...":
        personality = st.text_input("Type any character you want (e.g., Yoda, Iron Man):")

    mood = st.select_slider("Set their mood:", options=["Calm", "Sarcastic", "Chaotic"])
    
    st.markdown("---")
    st.caption("Change character to clear the chat history.")

load_dotenv()
client = genai.Client(api_key=os.getenv("API_KEY"))

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [] 

if "current_character" not in st.session_state:
    st.session_state.current_character = personality
elif st.session_state.current_character != personality:
    st.session_state.chat_history = []
    st.session_state.current_character = personality

for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"**You:** {chat['content']}")
    else:
        st.info(f"**{personality}:** {chat['content']}")

st.write("---") 

user_message = st.text_input("Say something: ")

if st.button("SEND"):
    if user_message and personality:
        
        # Save the user's message immediately
        st.session_state.chat_history.append({"role": "user", "content": user_message})
        
        ai_instructions = (
            f"You are acting as {personality}. Your current mood is {mood}. "
            f"Respond to the message sent by the user staying completely in character. "
            f"User message: {user_message}"
        )
        
        with st.spinner("Connecting to the multiverse!......"):
            # ADDED: try-except block to handle server drops smoothly
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=ai_instructions
                )
                
                # Save the AI's response to the history only if it succeeded
                st.session_state.chat_history.append({"role": "ai", "content": response.text})
                
                # Fun effects
                if personality == "A crazy Ronaldo fan":
                    st.balloons()
                elif personality == "An expert Hacker":
                    st.snow()

                # Refresh the page so the new messages show up instantly
                st.rerun()

            except Exception as e:
                # If Google's server fails, show a clean message instead of a crash screen
                st.error("The multiverse portal is temporarily overloaded! Please wait a moment and click SEND again.")
                
                # Optional: Print the actual error to your terminal for backend tracking
                print(f"API Error: {e}")
    
    else:
        st.warning("Please type a message and make sure a character is selected first!")