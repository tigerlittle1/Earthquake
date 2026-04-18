import streamlit as st
import datetime
from data.get_data import EarthquakeData
from ui.components import EarthquakeInfoCard
from utils.router import init_page, current_page

st.set_page_config(page_title="Earthquake Dashboard", layout="wide")

st.title("🌏 地震研究 Dashboard")

# 初始化頁面
init_page("latest")

# ====== 日期（自動抓最近 7 天） ======
default_end = datetime.date.today()
default_start = default_end - datetime.timedelta(days=30)

start = st.sidebar.date_input("開始日期", value=default_start)
end = st.sidebar.date_input("結束日期", value=default_end)

# 自動對調
if start > end:
    start, end = end, start

start_str = start.strftime("%Y-%m-%d")
end_str = end.strftime("%Y-%m-%d")

# ====== 最小震級 ======
minmag = st.sidebar.slider("最小震級", 0.0, 10.0, 1.0)

# ====== 抓資料 ======
eq = EarthquakeData()
df = eq.get_taiwan_data(start_str, end_str, minmag=minmag)

if df.empty:
    st.warning("沒有資料")
    st.stop()

# 最新地震
latest = df.sort_values("time", ascending=False).iloc[0].to_dict()

# ====== 建立卡片物件 ======
card = EarthquakeInfoCard(latest, df)

# ====== 主畫面切換 ======
page = current_page()

if page == "latest":
    card.render_latest()

elif page == "map":
    card.render_map_page()