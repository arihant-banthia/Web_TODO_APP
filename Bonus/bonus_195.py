import streamlit as st
from PIL import Image
# PIL represents pillow library
st.subheader("Color to Grayscale Converter")

uploaded_img = st.file_uploader("Upload Image ")

with st.expander("Start Camera"):
    camera_img = st.camera_input("Camera")
    # captures the image through our web-cam
if camera_img:
    # create a pillow image instance
    img = Image.open(camera_img)
    # convert into grayscale
    gray_img = img.convert("L")
    # Render the grayscale image on the web
    st.image(gray_img)

if uploaded_img:
    img = Image.open(uploaded_img)
    gray_uploaded_img = img.convert("L")
    st.image(gray_uploaded_img)