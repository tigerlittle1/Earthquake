import streamlit as st
import plotly.graph_objects as go
def latest_earthquake_card(latest):
    """
    最新地震卡片（研究者 + 現代儀表板風格）
    latest: dict
    """

    st.subheader("🔴 最新地震 Latest Earthquake")

    # 主要資訊區
    st.markdown(f"""
    **時間（UTC）**：{latest['time']}  
    **地點**：{latest['place']}  
    **震級**：{latest['mag']} Mw  
    **深度**：{latest['depth']} km  
    **類型**：{latest['type']}  
    **經緯度**：{latest['longitude']}°E, {latest['latitude']}°N  
    """)

    # 視覺化：震級 bar
    mag_fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=latest["mag"],
        gauge={'axis': {'range': [0, 10]}},
        title={'text': "震級 Magnitude"}
    ))
    mag_fig.update_layout(height=200, margin=dict(l=20, r=20, t=40, b=0))

    # 視覺化：深度 bar
    depth_fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=latest["depth"],
        gauge={'axis': {'range': [0, 700]}},
        title={'text': "深度 Depth (km)"}
    ))
    depth_fig.update_layout(height=200, margin=dict(l=20, r=20, t=40, b=0))

    col1, col2 = st.columns(2)
    col1.plotly_chart(mag_fig, use_container_width=True)
    col2.plotly_chart(depth_fig, use_container_width=True)

    # 操作按鈕
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    c1.button("在地圖上顯示")
    c2.button("查看附近事件")
    c3.button("查看趨勢")