import streamlit as st
from PIL import Image

cam_image = st.camera_input("Camera")
if cam_image:
    img = Image.open(cam_image)
    gray_img = img.convert("L")
    st.image(gray_img)
