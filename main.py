#!/usr/bin/env python
from os import path, mkdir
from reduce_data import reduce_data
from graph_generator import graph_generator
from hotspot_analysis import hotspot_analysis


def create_folders(save_to) -> None:
  if not path.exists("output"):
    mkdir("output")
  for i in ["graficos", "mapas"]:
    if not path.exists(path.join("output", i)):
      mkdir(path.join("output", i))
    mkdir(path.join("output", i, save_to))
    if i == "graficos":
      for j in ["barra", "pizza"]:
        mkdir(path.join("output", i, save_to, j))


def main() -> None:
  csv_file = "data/Traffic_Crashes_-_Crashes.csv"
  xlsx_files = ["antigo.xlsx", "recente.xlsx"]

  for file in xlsx_files:
    file_path = path.join("data", file)
    file_name = file.split(".")[0]

    if not path.exists(file_path):
      if not path.exists(csv_file):
        print("O arquivo para ser reduzido não existe; Saindo...")
        quit()
      print(f"Reduzindo arquivo {csv_file} para {file_path}.")
      reduce_data(csv_file, file_path)
    else:
      create_folders(save_to=file_name)

      print(f"Gerando gráficos ({file_name}).")
      graph_generator(file_path, save_to=file_name)

      print(f"Gerando mapas de Hotspot ({file_name}).")
      hotspot_analysis(file_path, save_to=file_name, algorithm="kmeans")


if __name__ == "__main__":
  main()
