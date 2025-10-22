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
st.write(f"選擇的軟體是: {option}")
st.write(f"選擇的年份是: {year}")
#  (Button)
if st.button("s!"):
 st.balloons()
#  (File Uploader)
uploaded_file = st.file_uploader(
"上船你的 Shapefile (.zip) 或 GeoTIFF (.tif) 或 GeoJSON (.json)",
type=["zip", "tif", "json"]
)
if uploaded_file is not None:
 st.success(f"你上傳了: {uploaded_file.name} (大小: {uploaded_file.size} bytes)")
