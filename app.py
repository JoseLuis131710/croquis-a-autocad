import streamlit as st
from PIL import Image
import cv2
import numpy as np

st.set_page_config(page_title="Croquis a AutoCAD")

st.title("Croquis a Plano CAD")

archivo = st.file_uploader(
    "Sube una imagen",
    type=["png","jpg","jpeg"]
)

if archivo:

    imagen = Image.open(archivo)

    st.image(imagen)

    img = np.array(imagen)

    gris = cv2.cvtColor(
        img,
        cv2.COLOR_RGB2GRAY
    )

    _, binaria = cv2.threshold(
        gris,
        150,
        255,
        cv2.THRESH_BINARY_INV
    )

    contornos, _ = cv2.findContours(
        binaria,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    resultado = img.copy()

    cv2.drawContours(
        resultado,
        contornos,
        -1,
        (0,255,0),
        2
    )

    st.image(resultado)

    st.success("Plano detectado")
