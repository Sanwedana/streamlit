import streamlit as st

st.title("My First Streamlit Calculator!!")
st.write("Welcome! Let's do some math.")

num1 = st.number_input("Enter your first number:", value=0.0)
num2 = st.number_input("Enter your second number:", value=0.0)

operation = st.selectbox(
    "What would you like to do?",
    ("Add (+)", "Subtract (-)", "Multiply (*)", "Divide (/)")
)

if st.button("Calculate"):
    
    if operation == "Add (+)":
        result = num1 + num2
        st.success(f"The answer is: {result}")
        
    elif operation == "Subtract (-)":
        result = num1 - num2
        st.success(f"The answer is: {result}")
        
    elif operation == "Multiply (*)":
        result = num1 * num2
        st.success(f"The answer is: {result}")
        
    elif operation == "Divide (/)":
        if num2 == 0:
            st.error("Oops! You cannot divide by zero.")
        else:
            result = num1 / num2
            st.success(f"The answer is: {result}")