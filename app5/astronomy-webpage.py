import streamlit as st
import requests

api_key = "lOMeLLcyC10XQadpMM5dnTGER185bTbKajlRm5Nu"
url_text = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
response1 = requests.get(url_text)
data = response1.json()
st.title(data["title"])

url_image = "https://api.nasa.gov/assets/img/general/apod.jpg"
response2 = requests.get(url_image)
data_img = response2.content

with open("image_astro.jpg","wb") as f:
    f.write(data_img)

st.image("image_astro.jpg")
st.write(data["explanation"])