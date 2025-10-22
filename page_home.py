import streamlit as st
# 展示內容
st.title("歡迎來到專案")
st.write("這是使用Streamlit建立互動地圖應用程式")

video_url = "https://i.imgur.com/1GoAB0C.mp4"
st.write(f"正在播放影片 {video_url}")
st.video(video_url)

image_url = "https://i.imgur.com/uf1T4ND.png"
st.image(image_url)
