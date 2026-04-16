import streamlit as st
from data.get_data import EarthquakeData
from ui.ui_latest import latest_earthquake_card
from visualizer.map import plot_single_point
from streamlit_folium import st_folium

st.set_page_config(page_title="Earthquake Dashboard", layout="wide")

st.title("🌏 地震研究 Dashboard")

# 日期
start = st.sidebar.date_input("開始日期")
end = st.sidebar.date_input("結束日期")
if start > end:
    start, end = end, start

start_str = start.strftime("%Y-%m-%d")
end_str = end.strftime("%Y-%m-%d")

minmag = st.sidebar.slider("最小震級", 0.0, 10.0, 4.0)

# 抓資料
eq = EarthquakeData()
df = eq.get_taiwan_data(start_str, end_str, minmag=minmag)

if df.empty:
    st.warning("沒有資料")
    st.stop()

latest = df.sort_values("time", ascending=False).iloc[0].to_dict()

# 初始化 session_state
if "show_map" not in st.session_state:
    st.session_state["show_map"] = False

# ⭐ 按鈕事件
latest_earthquake_card(latest,df)

# ⭐ 如果按下「在地圖上顯示」
if st.session_state["show_map"]:
    st.subheader("📍 地震位置")
    m = plot_single_point(
        latest["latitude"],
        latest["longitude"],
        latest["place"],
        latest["mag"],
        latest["depth"]
    )
    st_folium(m, width=700, height=500)
