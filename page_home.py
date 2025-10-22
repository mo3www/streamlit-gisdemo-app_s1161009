import streamlit as st
# 展示內容
st.title("林彥伶")
st.header("GIS專題")
st.write("來自資管系的一個互動式地圖瀏覽器")

video_url = "https://i.meee.com.tw/TuZ68Gp.gif"
st.write(f"正在播放影片 {video_url}")
st.video(video_url)

image_url = "https://i.imgur.com/uf1T4ND.png"
st.image(image_url)
