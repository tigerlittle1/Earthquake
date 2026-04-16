import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

def latest_earthquake_card(latest, df):
    st.subheader("🔴 最新地震 Latest Earthquake")

    # 轉換時間
    utc_time = latest["time"]
    local_time = utc_time + timedelta(hours=8)

    # 事件摘要
    st.markdown(f"""
    ### **{latest['mag']} Mw**  
    **深度**：{latest['depth']} km  
    **類型**：{latest['type']}  
    """)

    st.markdown(f"""
    **時間（UTC）**：{utc_time}  
    **時間（本地）**：{local_time}  
    **地點**：{latest['place']}  
    **經緯度**：{latest['longitude']}°E, {latest['latitude']}°N  
    """)

    # 上下文資訊
    last_24h = df[df["time"] >= utc_time - timedelta(hours=24)]
    last_7d = df[df["time"] >= utc_time - timedelta(days=7)]

    st.markdown("---")
    st.markdown(f"""
    **過去 24 小時事件**：{len(last_24h)}  
    **過去 7 天事件**：{len(last_7d)}  
    **是否為餘震**：{"是" if latest['mag'] < last_24h['mag'].max() else "否"}  
    **深度分類**：{depth_category(latest['depth'])}  
    """)

    # 視覺化
    col1, col2 = st.columns(2)

    col1.plotly_chart(
        go.Figure(go.Indicator(
            mode="gauge+number",
            value=latest["mag"],
            gauge={'axis': {'range': [0, 10]}},
            title={'text': "震級 Magnitude"}
        )),
        width='stretch'
    )

    col2.plotly_chart(
        go.Figure(go.Indicator(
            mode="gauge+number",
            value=latest["depth"],
            gauge={'axis': {'range': [0, 700]}},
            title={'text': "深度 Depth (km)"}
        )),
        width='stretch'
    )

    # 按鈕
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    if c1.button("在地圖上顯示"):
        st.session_state["show_map"] = True

    if c2.button("查看附近事件"):
        st.session_state["show_map"] = False

    if c3.button("查看趨勢"):
        st.session_state["show_map"] = False
    #
    # show_map = c1.button("在地圖上顯示")
    # show_event = c2.button("查看附近事件")
    # show_trend = c3.button("查看趨勢")
    # return show_map, show_event, show_trend


def depth_category(depth):
    if depth < 10:
        return "極淺層地震"
    elif depth < 70:
        return "淺層地震"
    elif depth < 300:
        return "中層地震"
    else:
        return "深層地震"