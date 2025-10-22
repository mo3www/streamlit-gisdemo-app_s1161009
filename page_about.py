import streamlit as st
import pandas as pd
st.title("Streamlit 核心 Widgets")
# 1. 把 Widgets 放到側欄 (sidebar)
with st.sidebar:
 st.header("這裡是側欄")
#  (Selectbox)
option = st.selectbox(
"你喜歡的 GIS 軟體?",
("QGIS", "ArcGIS", "ENVI", "GRASS")
)
#  (Slider)
year = st.slider("選擇年份:", 1990, 2030, 2024)
# 2. 顯示 Widgets 結果
st.write(f"oöo: {option}")
st.write(f"oö~o: {year}")
#  (Button)
if st.button("s!"):
 st.balloons()
# þNó (File Uploader) - vß!
uploaded_file = st.file_uploader(
"Nóoö Shapefile (.zip) v GeoTIFF (.tif) v GeoJSON (.json)",
type=["zip", "tif", "json"]
)
if uploaded_file is not None:
 st.success(f"oNó: {uploaded_file.name} (//: {uploaded_file.size} bytes)")
