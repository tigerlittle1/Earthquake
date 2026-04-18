import streamlit as st
from datetime import timedelta
from utils.router import go_page
from ui.ui_gauge import GaugePanel
from ui.ui_map import MapPanel

class EarthquakeInfoCard:
    def __init__(self, latest, df):
        self.latest = latest
        self.df = df
        self.utc_time = latest["time"]
        self.local_time = self.utc_time + timedelta(hours=8)

        # Panels
        self.gauge_panel = GaugePanel(latest)
        self.map_panel = MapPanel(latest)

    # ====== 深度分類 ======
    def depth_category(self, depth):
        if depth < 10:
            return "極淺層地震"
        elif depth < 70:
            return "淺層地震"
        elif depth < 300:
            return "中層地震"
        else:
            return "深層地震"

    # ====== 上下文資訊 ======
    def context_info(self):
        utc_time = self.utc_time
        last_24h = self.df[
            (self.df["time"] >= utc_time - timedelta(hours=24)) &
            (self.df["time"] < utc_time)
            ]
        last_7d = self.df[
            (self.df["time"] >= utc_time - timedelta(days=7)) &
            (self.df["time"] < utc_time)
            ]
        return last_24h, last_7d
    # ====== 資訊卡 ======
    def render_info(self, show_back=False, show_map_button=False):
        st.subheader("🔴 最新地震 Latest Earthquake")

        latest = self.latest
        last_24h, last_7d = self.context_info()

        st.markdown(f"""
        ### **{latest['mag']} Mw**
        **深度**：{latest['depth']} km  
        **類型**：{latest['type']}  

        **時間（UTC）**：{self.utc_time}  
        **時間（本地）**：{self.local_time}  
        **地點**：{latest['place']}  
        **經緯度**：{latest['longitude']}°E, {latest['latitude']}°N  
        """)

        st.markdown("---")
        st.markdown(f"""
        **過去 24 小時事件**：{len(last_24h)}  
        **過去 7 天事件**：{len(last_7d)}  
        **是否為餘震**：{"是" if latest['mag'] < last_24h['mag'].max() else "否"}  
        **深度分類**：{self.depth_category(latest['depth'])}  
        """)

        st.markdown("---")

        if show_map_button:
            st.button("在地圖上顯示", on_click=lambda: go_page("map"))

        if show_back:
            st.button("返回", on_click=lambda: go_page("latest"))

    # ====== 最新地震頁 ======
    def render_latest(self):
        col_info, col_vis = st.columns([1, 1])

        with col_info:
            self.render_info(show_map_button=True)

        with col_vis:
            self.gauge_panel.render()

    # ====== 地圖頁 ======
    def render_map_page(self):
        col_info, col_vis = st.columns([1, 2])

        with col_info:
            self.render_info(show_back=True)

        with col_vis:
            self.map_panel.render()