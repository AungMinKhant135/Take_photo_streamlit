import streamlit as st

st.header("Taking Photo")
st.subheader("Say-------Cheeseeeee-----")

picture = st.camera_input("Take a picture")

if picture:
     st.image(picture)