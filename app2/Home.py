import streamlit as st
import pandas


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col2:
    st.title("Hi, I'm Anuj ")
    content = """
    I'm a Computer
    Science student based
    in Amrita Vishwa Vidyapeetham
    Welcome to my portfolio page, where I showcase my journey and achievements
    in the realm of technology and computer science. 
    I'm passionate about leveraging technology to solve real-world challenges.
    """
    st.info(content)

with col1:
    st.image(r"C:\Users\Anuj\Desktop\python-20app-course\app2\images\image_mine.jpg")

write_content = """
Below you can find some of the apps which I built. Feel free to contact me :)
"""

st.info(write_content)

df = pandas.read_csv(r"C:\Users\Anuj\Desktop\python-20app-course\app2\data.csv", sep=";")

col3, col_emp, col4 = st.columns([3, 1, 3])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(rf'C:\Users\Anuj\Desktop\python-20app-course\app2\images\{row["image"]}')
        st.write(f'[source code]({row["url"]})')

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(rf'C:\Users\Anuj\Desktop\python-20app-course\app2\images\{row["image"]}')
        st.write(f'[source code]({row["url"]})')

