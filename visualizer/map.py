import folium
from data.get_data import EarthquakeData
def plot_taiwan_map(df_tw, output="taiwan_earthquakes.html"):
    """
    使用 folium 畫出台灣地震地圖
    - df_tw: 台灣地震 DataFrame
    - output: 輸出 HTML 檔案名稱
    """

    # 台灣中心點（大約）
    taiwan_center = [23.7, 121]

    m = folium.Map(location=taiwan_center, zoom_start=7)

    # 顏色依照震級變化
    def mag_color(mag):
        if mag >= 6:
            return "red"
        elif mag >= 5:
            return "orange"
        elif mag >= 4:
            return "yellow"
        else:
            return "green"

    # 在地圖上畫點
    for _, row in df_tw.iterrows():
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=max(row["mag"] * 1.5, 3),  # 震級越大點越大
            color=mag_color(row["mag"]),
            fill=True,
            fill_opacity=0.7,
            popup=f"{row['time']}<br>{row['place']}<br>Mag: {row['mag']}"
        ).add_to(m)

    # # 輸出 HTML
    # m.save(output)
    return m

def plot_single_point(lat, lon, place, mag, depth):
    m = folium.Map(location=[lat, lon], zoom_start=7)

    folium.CircleMarker(
        location=[lat, lon],
        radius=max(mag * 1.5, 5),
        color="red",
        fill=True,
        fill_opacity=0.8,
        popup=f"{place}<br>Mag: {mag}<br>Depth: {depth} km"
    ).add_to(m)

    return m


if __name__ == "__main__":
    eq = EarthquakeData()

    start = "2024-01-01"
    end = "2025-01-01"

    print(f"下載 {start} ~ {end} 的地震資料...")
    # 台灣資料
    df_tw = eq.get_taiwan_data(start, end, minmag=4)
    print(f"台灣地震筆數：{len(df_tw)}")

    # 畫地圖
    plot_taiwan_map(df_tw)