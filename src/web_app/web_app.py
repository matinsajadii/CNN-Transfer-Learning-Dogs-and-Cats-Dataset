import streamlit as st
import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import matplotlib.pyplot as plt
import numpy as np



def load_classification_model():
    # Load the pre-trained model
    model = tf.keras.models.load_model("../best_model/InceptionV3.h5")
    return model

model = load_classification_model()



st.image("https://storage.googleapis.com/kaggle-media/competitions/kaggle/3362/media/woof_meow.jpg", use_column_width=True)
st.title("Dog or Cat Image Classifier")

uploaded_file = st.file_uploader("Upload an image of a dog or a cat", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = load_img(uploaded_file, target_size=(224, 224))
    img_array = img_to_array(image)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        prediction = model.predict(img_array)
        if prediction > 0.5:
            st.write("Prediction: Dog")
        else:
            st.write("Prediction: Cat")
