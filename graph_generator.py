import json
import matplotlib.pyplot as plt
import pandas as pd


def json_to_dict(file_path: str) -> dict:
  with open(file_path, "r", encoding="utf8") as json_file:
    return json.load(json_file)


# Função para gerar um gráfico de barras
def grafico_barra(
  df, column, color, xlabel, ylabel, title, xticks_rotation, save_to
) -> None:
  acidentes = df[column].value_counts()
  title = f"{ylabel} por {xlabel}" if title == "" else title
  file_name = f"acidentes_{xlabel.lower().replace(' ', '_')}"
  save_path = f"output/graficos/{save_to}/barra/" + file_name.replace("?", "") + ".png"

  plt.figure(figsize=(10, 6))
  bars = acidentes.plot(kind="bar", color=color)

  for bar in bars.patches:
    bars.annotate(
      f"{bar.get_height()}",
      (bar.get_x() + bar.get_width() / 2, bar.get_height()),
      ha="center",
      va="bottom",
    )

  plt.title(title)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.xticks(rotation=xticks_rotation)
  plt.grid(True)
  plt.savefig(save_path, bbox_inches="tight")
  plt.close()
  print(f"  Gráfico de barras salvo como '{save_path}'.")


# Função para gerar um gráfico de pizza
def grafico_pizza(df, column, title, save_to) -> None:
  acidentes = df[column].value_counts()
  file_name = f"acidentes_{title.lower().replace(' ', '_')}"
  save_path = f"output/graficos/{save_to}/pizza/" + file_name + ".png"

  plt.figure(figsize=(8, 8))
  plt.pie(
    acidentes,
    labels=acidentes.index,
    autopct="%1.1f%%",
    startangle=140,
    colors=plt.cm.Paired.colors,
  )
  plt.title(title)
  plt.savefig(save_path, bbox_inches="tight")
  plt.close()
  print(f"  Gráfico de pizza salvo como '{save_path}'.")


def graph_generator(xlsx_file, save_to) -> None:
  graph_settings = json_to_dict("graph_settings.json")

  df = pd.read_excel(xlsx_file, sheet_name="Sheet1", header=0)
  df = df.dropna(axis=1, how="all")

  for i in graph_settings["graphs"]:
    grafico_barra(
      df=df,
      column=i["column"],
      color=i["color"],
      xlabel=i["xlabel"],
      ylabel=i["ylabel"],
      title=i["bar_title"],
      xticks_rotation=i["xticks"],
      save_to=save_to,
    )
    grafico_pizza(
      df=df,
      column=i["column"],
      title=i["pizza_title"],
      save_to=save_to,
    )
