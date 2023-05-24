import streamlit as st
import pandas as pd

from PIL import Image

def main():
    st.title('내 앱 대시보드')

    # 사진과 영상을 보여주는 방법

    img = Image.open('data/image_03.jpg')

    print(img)

    st.image(img)

    st.image(img, use_column_width=True)

    # 이미지 URL 로 불러와서 보여주기
    st.image('https://cdn.epnc.co.kr/news/photo/201907/91021_81259_3048.jpg')

    video_file = open('data/video1.mp4','rb')
    st.video(video_file)

if __name__ == '__main__' :
    main()