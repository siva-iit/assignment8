import streamlit as st
import pandas as pd

st.title("Find the largest among the 3 given numbers")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3 = st.number_input("Enter the third number:")

def largest_number(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3
    return largest

if st.button("Find the Largest Number"):
    result = largest_number(num1, num2, num3)
    st.write("The largest number is:", result)
