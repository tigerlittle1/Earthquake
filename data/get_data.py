import requests
import pandas as pd

class EarthquakeData:
    """
    EarthquakeData
    ---------------
    用來從 USGS Earthquake Catalog API 下載地震資料的工具類別。

    功能：
    - 透過 USGS API 取得指定時間範圍的地震資料
    - 支援最小震度篩選
    - 自動解析 GeoJSON 格式
    - 回傳 pandas DataFrame，方便後續分析與視覺化

    參考：
    https://earthquake.usgs.gov/fdsnws/event/1/
    """

    def __init__(self, url="https://earthquake.usgs.gov/fdsnws/event/1/query", format="geojson"):
        """
        初始化 EarthquakeData 物件。

        參數：
        - url: USGS API endpoint
        - format: 回傳格式（預設 geojson）
        """
        self.url = url
        self.format = format

    def _get_data(self, starttime, endtime, minmag=5):
        """
        向 USGS API 發送請求，取得原始地震資料（GeoJSON）。

        參數：
        - starttime: 起始時間（YYYY-MM-DD）
        - endtime: 結束時間（YYYY-MM-DD）
        - minmag: 最小震度（預設 5）

        回傳：
        - dict（GeoJSON）
        """
        params = {
            "format": self.format,
            "starttime": starttime,
            "endtime": endtime,
            "minmagnitude": minmag
        }

        res = requests.get(self.url, params=params)

        # 基本錯誤處理
        if res.status_code != 200:
            raise Exception(f"USGS API Error: {res.status_code}")

        return res.json()

    def parse_geojson(self, res):
        """
        將 USGS GeoJSON 解析成 pandas DataFrame。

        欄位包含：
        - time（轉換成 datetime）
        - place（地點描述）
        - mag（震級）
        - latitude / longitude（經緯度）
        - depth（深度，公里）

        回傳：
        - pandas DataFrame
        """
        features = res.get("features", [])
        if not features:
            return pd.DataFrame()

        records = []
        for feature in features:
            props = feature["properties"]
            geom = feature["geometry"]

            records.append({
                "time": pd.to_datetime(props["time"], unit="ms"),  # USGS 時間是毫秒 timestamp
                "place": props["place"],
                "mag": props["mag"],
                "longitude": geom["coordinates"][0],
                "latitude": geom["coordinates"][1],
                "depth": geom["coordinates"][2],
                "type": props.get("type", "earthquake")
            })

        return pd.DataFrame(records)

    def get_data(self, starttime, endtime, minmag=5):
        """
        取得指定時間範圍的地震資料（DataFrame）。

        參數：
        - starttime: 起始時間（YYYY-MM-DD）
        - endtime: 結束時間（YYYY-MM-DD）
        - minmag: 最小震度

        回傳：
        - pandas DataFrame
        """
        res = self._get_data(starttime, endtime, minmag)
        return self.parse_geojson(res)

        # ---------------------------------------------------------
        # ⭐ 新增：台灣地震篩選功能
        # ---------------------------------------------------------
    def get_taiwan_data(self, starttime, endtime, minmag=5):
        """
        篩選台灣範圍內的地震資料。
        台灣大致經緯度範圍：
        - 經度：119 ~ 123
        - 緯度：21 ~ 26
        """
        df = self.get_data(starttime, endtime, minmag)
        lon_min, lon_max = 119, 123
        lat_min, lat_max = 21, 26

        return df[
            (df["longitude"] >= lon_min) &
            (df["longitude"] <= lon_max) &
            (df["latitude"] >= lat_min) &
            (df["latitude"] <= lat_max)
                ]


if __name__ == "__main__":
    """
    測試 EarthquakeData 是否能正常運作：
    - 呼叫 USGS API
    - 抓取指定時間範圍的地震資料
    - 回傳 pandas DataFrame
    - 印出前 5 筆資料與總筆數
    """

    eq = EarthquakeData()

    # 測試用日期（你可以改成任何日期）
    start = "2024-01-01"
    end = "2025-01-01"

    print(f"正在下載 {start} ~ {end} 的地震資料...")

    try:
        df = eq.get_taiwan_data(start, end, minmag=3)

        if df.empty:
            print("⚠ 沒有找到任何地震資料")
        else:
            print("✅ 下載成功！")
            print(df.head())
            print(f"\n總筆數：{len(df)}")

    except Exception as e:
        print("❌ 發生錯誤：", e)