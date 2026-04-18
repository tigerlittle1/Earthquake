import streamlit as st

# 初始化 page 狀態
def init_page(default="latest"):
    if "page" not in st.session_state:
        st.session_state.page = default

# 切換頁面
def go_page(page_name: str):
    st.session_state.page = page_name

# 取得目前頁面
def current_page():
    return st.session_state.page