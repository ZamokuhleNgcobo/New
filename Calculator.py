#install streamlit
import streamlit as st

st.title("Calculator")

# creates a horizontal line
st.write("---")
 
# input 1
num1 = st.number_input(label="Enter first number")
 
# input 2
num2 = st.number_input(label="Enter second number")

st.write("Operation")
 
operation = st.radio("Select an operation to perform:",
                    ("*", "+", "/", "-"))
ans = 0


def calculator():
    if operation == "*":
        answer = num1 * num2
        
        
    elif a == "+":
        answer = num1 + num2
        
    elif a== "-":
        answer = num1 - num2 
        
        
    elif a == "/" and num2!=0:
        answer = num1 / num2
    else:
        st.warning("Division by 0 error. Please enter a non-zero number.")
        answer = "Not defined"
        
    st.success(f"Answer = {ans}")
 
if st.button("Calculate"):
    calculate()




