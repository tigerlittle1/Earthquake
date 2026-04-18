# 🌏 Earthquake Research Dashboard

一個為研究者打造的地震資料分析 Dashboard。
採用 Class-based UI + Panel 模組化 + Router 多頁式架構，提供最新地震資訊、地圖視覺化、儀表圖與上下文分析。


## 📁 專案結構

```text
Earthquake/
│
├── app.py                         # 主入口（Router + Page Switch）
│
├── data/
│   └── get_data.py                # 取得 USGS 地震資料
│
├── ui/
│   ├── components.py              # EarthquakeInfoCard（主 UI Class）
│   ├── ui_gauge.py                # GaugePanel（儀表圖 Panel）
│   └── ui_map.py                  # MapPanel（地圖 Panel）
│
├── utils/
│   └── router.py                  # 頁面切換 Router
│
└── visualizer/
    └── map.py                     # Folium 地圖繪製
```

---

## 🚀 執行方式

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔍 功能特色
### ✔ Class-based UI（EarthquakeInfoCard）
統一管理：
- 地震摘要（震級、深度、類型、時間、地點）
- 上下文分析（24 小時事件、7 天事件、餘震判斷、深度分類）
- 自動切換頁面（最新地震頁 / 地圖頁）
- 與 Panel 組合（儀表圖、地圖）

### ✔ Panel 模組化（ui_gauge.py / ui_map.py）
UI 拆成可重複使用的 Panel：
- GaugePanel：震級與深度儀表圖
- MapPanel：Folium 地圖顯示
未來可自由組合成不同頁面（趨勢頁、附近事件頁等）。
- 
### ✔ Router（utils/router.py）
乾淨的頁面切換：
- latest → 最新地震頁
- map → 地圖頁
按鈕使用 on_click，避免按兩次才切換的問題。


---

##📌 目前頁面
### 🔴 最新地震頁（Latest）
- 	最新地震摘要
- 	24 小時 / 7 天事件統計
- 	餘震判斷
- 	深度分類
- 	震級儀表圖
- 	深度儀表圖
- 	「在地圖上顯示」按鈕
### 📍 地圖頁（Map）
-	最新地震資訊
- 	Folium 地圖
-	「返回」按鈕

## 🧩 使用技術

- Python 3.x
- Streamlit
- Folium
- Plotly
- Pandas
- USGS Earthquake API

---

## 📌 TODO

- [ ] 趨勢頁（時間序列、震級分布）
- [ ] 附近事件分析（距離計算 + 地圖）
- [ ] 事件列表頁（可排序 DataFrame）
- [ ] 熱點分析（KDE）
- [ ] 多事件地圖（24 小時 / 7 天 overlay）
- [ ] 震源機制（Beachball）

