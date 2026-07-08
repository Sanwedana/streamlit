import streamlit as st
st.title("Echo Chamber 9000")
st.write("Welcome to the Echo Chamber 9000! Type something below and see it echoed back to you.")
user_name = st.text_input("Your Name:")
user_message = st.text_input("Message:")

if st.button("Transmit"):
    if not user_name:
        st.error("Please provide your name.")
    elif not user_message:
        st.warning("Please type a message to transmit.")
    else: 
        st.success(f"Transmission successful! Greetings, {user_name}. We received your message: {user_message}")
        char_length = len(user_message)
        token_count = char_length / 4 
        
        st.info(f"System Check: Your message will consume approximately {token_count} tokens from our context window.")