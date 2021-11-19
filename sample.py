import streamlit as st
import pandas as pd
import numpy as np
import cv2

menu = ['home', 'about me', 'read data', 'camera']
choice = st.sidebar.selectbox('Menu', menu)
if choice == 'home':
    st.write('Hello')
    st.header('First webapp')
    st.image('media\dog-beach-lifesaver.png')
    col1, col2 = st.columns(2)
    with col1:
        dog_name = st.text_input('What is your dog name?')
        st.write('Your dog name:', dog_name)
    with col2:
        age = st.slider('Dog age:', min_value=1, max_value=20)
        st.write('Your dog age:', age)
elif choice == 'read data':
    df = pd.read_csv('media\AB_NYC_2019.csv')
    st.dataframe(df)
elif choice == 'about me':
    fileup = st.file_uploader('upload file', type = ['jpg', 'png', 'jpeg'])
    st.image(fileup)
elif choice == 'camera':
    cam = cv2.VideoCapture(0) # device 0. If not work, try with 1 or 2

    if not cam.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cam.read()
        frame = cv2.flip(frame, 1)
        
        cv2.imshow('My App!', frame)

        key = cv2.waitKey(1) & 0xFF
        if key==ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()
