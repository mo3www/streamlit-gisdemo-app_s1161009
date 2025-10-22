# ...existing code...
import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import requests
import tempfile

st.set_page_config(layout="wide")
st.title("Leafmap + GeoPandas")

url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"

st.info("Downloading Natural Earth countries (110m)...")
try:
    resp = requests.get(url, stream=True, timeout=30)
    resp.raise_for_status()
    with tempfile.NamedTemporaryFile(suffix=".zip") as tmp:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk:
                tmp.write(chunk)
        tmp.flush()
        gdf = gpd.read_file(f"zip://{tmp.name}")
    st.dataframe(gdf.head())
except Exception as e:
    st.error(f"無法載入資料: {e}")
    st.stop()

m = leafmap.Map(center=[0, 0], zoom=2)

m.add_gdf(
    gdf,
    layer_name="Natural Earth countries (110m)",
    style={"fillOpacity": 0, "color": "black", "weight": 0.5},
    highlight=False,
)

m.add_layer_control()
m.to_streamlit(height=700)
# ...existing code...