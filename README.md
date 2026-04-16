# 🌏 Earthquake Research Dashboard

一個為研究者打造的地震資料分析 Dashboard。
整合 USGS API、互動式地圖、最新地震資訊卡片與篩選器，使用 Streamlit 建構，結構清晰、易於擴充。


## 📁 專案結構

```text
Earthquake/
│
├── app.py                 # 主入口點（Streamlit）
│
├── data/
│   └── get_data.py        # 取得 USGS 地震資料
│
├── ui/
│   └── ui_last.py         # 最新地震資訊卡片 UI
│
└── visualizer/
    ├── map.py             # 地圖繪製（Folium）
    └── taiwan_earthquakes.html (optional)
```

---

## 🚀 執行方式

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔍 功能特色

### ✔ 最新地震卡片
- 震級、深度、地點、時間（UTC + 本地）
- 自動分類（深度分類、事件分類）
- 24 小時 / 7 天事件統計
- Plotly 視覺化

### ✔ 篩選器
- 開始日期 / 結束日期（自動對調）
- 最小震級
- 自動抓取 USGS API

### ✔ 地圖顯示
- 按下「在地圖上顯示」即可顯示最新地震位置
- 使用 Folium + streamlit-folium
- 使用 session_state 避免地圖閃爍

---

## 🧩 使用技術

- Python 3.x
- Streamlit
- Folium
- Plotly
- Pandas
- USGS Earthquake API

---

## 📌 TODO

- [ ] 趨勢圖（時間序列、震級分布）
- [ ] 附近事件分析
- [ ] 多頁式 Dashboard
- [ ] 熱點分析（KDE）
- [ ] 完整事件表格（可排序）
- [ ] 自動切割查詢（避免 USGS 20k 限制）

