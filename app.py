# import necessary libraries
import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from transformers import pipeline
import torch
from PIL import Image

# define device computation
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# load finetuned model
pipe = pipeline("image-classification", model="aksara_model", device=device, top_k=20)

# define canvas
stroke_width = st.slider("Stroke width: ", 1, 25, 3)
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    background_color="#eee",
    update_streamlit=True,
    height=150,
    drawing_mode="freedraw",
    key="canvas",
)

# inference
if st.button("Predict"):
    img = Image.fromarray(canvas_result.image_data)
    results = pipe(img)
    top_1 = results[0]
    if top_1["score"] < 0.8:
        st.write("This is not aksara lampung")
    else:
        st.write(f'This is "{top_1["label"]}" with score: {top_1["score"]}')
