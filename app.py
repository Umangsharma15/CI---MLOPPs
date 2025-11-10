import streamlit as st

st.title("Power Calculator")
st.write("Enter a number to calculate its squire,cube,and fifth power.")

n= st.number_input("Enter an integer",value=1,step=1)

squire = n ** 2
cube = n ** 3
fifth_power = n**5
st.write(f"the squire of{n} is:{squire}")
st.write(f"the cube {n} is :{cube}")
st.write(f"the fifth power of {n} is :{fifth_power}")
