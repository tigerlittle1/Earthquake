import streamlit as st
import plotly.graph_objects as go

class GaugePanel:
    def __init__(self, latest):
        self.latest = latest

    def render(self):

        mag = self.latest["mag"]
        depth = self.latest["depth"]

        fig_mag = go.Figure(go.Indicator(
            mode="gauge+number",
            value=mag,
            gauge={'axis': {'range': [0, 10]}},
            title={'text': "震級 Magnitude"}
        ))

        fig_depth = go.Figure(go.Indicator(
            mode="gauge+number",
            value=depth,
            gauge={'axis': {'range': [0, 700]}},
            title={'text': "深度 Depth (km)"}
        ))

        c1, c2 = st.columns(2)
        c1.plotly_chart(fig_mag, use_container_width=True)
        c2.plotly_chart(fig_depth, use_container_width=True)