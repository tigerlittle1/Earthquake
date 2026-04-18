import streamlit as st
from streamlit_folium import st_folium
from visualizer.map import plot_single_point

class MapPanel:
    def __init__(self, latest):
        self.latest = latest
    def render(self):
        m = plot_single_point(
            self.latest["latitude"],
            self.latest["longitude"],
            self.latest["place"],
            self.latest["mag"],
            self.latest["depth"]
        )
        st_folium(m, width=700, height=500)