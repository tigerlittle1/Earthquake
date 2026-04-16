import requests
import pandas as pd

url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

params = {
    "format": "geojson",
    "starttime": "2024-01-01",
    "endtime": "2024-12-31",
    "minmagnitude": 5
}

res = requests.get(url, params=params).json()

# 解析 GeoJSON
records = []
for feature in res["features"]:
    props = feature["properties"]
    geom = feature["geometry"]

    records.append({
        "time": props["time"],
        "place": props["place"],
        "mag": props["mag"],
        "longitude": geom["coordinates"][0],
        "latitude": geom["coordinates"][1],
        "depth": geom["coordinates"][2]
    })

df = pd.DataFrame(records)
df.head()
print(df)