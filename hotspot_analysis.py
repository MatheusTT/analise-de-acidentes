import folium
import pandas as pd
from folium.plugins import HeatMap
from sklearn.cluster import DBSCAN, KMeans
from sklearn.preprocessing import StandardScaler


def get_clusters(df, algorithm="dbscan"):
  scaler = StandardScaler()
  data_scaled = scaler.fit_transform(df[["LATITUDE", "LONGITUDE"]])

  match algorithm:
    case "dbscan":
      algorithm = DBSCAN(eps=0.1, min_samples=10)
    case "kmeans":
      algorithm = KMeans(n_clusters=5, random_state=42)

  df["Cluster"] = algorithm.fit_predict(data_scaled)

  # Filtrar apenas clusters válidos (remover ruído, que geralmente é marcado como -1)
  return df[df["Cluster"] != -1]


def gen_hotspot_map(df, coords, file_name) -> None:
  fmap = folium.Map(location=coords, zoom_start=11)

  for _, row in df.iterrows():
    folium.CircleMarker(
      location=[row["LATITUDE"], row["LONGITUDE"]],
      radius=3,
      color="red",
      fill=True,
      fill_color="red",
      fill_opacity=0.6,
    ).add_to(fmap)

  fmap.save(file_name)
  print(f"  Mapa Hotspot salvo como '{file_name}'.")


def gen_hotspot_heatmap(df, coords, file_name) -> None:
  fmap = folium.Map(location=coords, zoom_start=11)
  heat_data = [[row["LATITUDE"], row["LONGITUDE"]] for _, row in df.iterrows()]
  HeatMap(heat_data).add_to(fmap)
  fmap.save(file_name)
  print(f"  Mapa de calor Hotspot salvo como '{file_name}'.")


def hotspot_analysis(xlsx_file, save_to, algorithm="kmeans") -> None:
  chicago_coords = [41.8781, -87.6298]
  df = pd.read_excel(xlsx_file)
  df = df[["LATITUDE", "LONGITUDE"]].dropna()
  file_name = f"output/mapas/{save_to}/hotspot_"
  clusters = get_clusters(df, algorithm=algorithm)

  gen_hotspot_map(
    df=clusters,
    coords=chicago_coords,
    file_name=file_name + "map.html",
  )
  gen_hotspot_heatmap(
    df=clusters,
    coords=chicago_coords,
    file_name=file_name + "heatmap.html",
  )
