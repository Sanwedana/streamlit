import streamlit as st
st.title("HELLO")
st.write("This is a simple Streamlit app that uses the Gemini API to generate content.") #its not the title
user_message = st.text_input("please enter here")
print(user_message)
if st.button("SUBMIT"):
    st.write(user_message)
    
