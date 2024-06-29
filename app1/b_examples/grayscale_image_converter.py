import streamlit as st
from PIL import Image

st.title("Color to GrayScale Converter ")
st.subheader("Choose your file below to see the grayscale version of it !")
image_upload = st.file_uploader("Choose file ")
if image_upload:
    st.subheader("Normal Photo ")
    st.image(image_upload)
    image_convert = Image.open(image_upload)
    img_final = image_convert.convert("L")
    st.subheader("Converted to Grayscale")
    st.image(img_final)
