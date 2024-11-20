import pandas as pd
from openpyxl import load_workbook


def resize_columns(arquivo_excel):
  workbook = load_workbook(arquivo_excel)
  sheet = workbook.active

  for col in sheet.columns:
    max_length = 0
    col_letter = col[0].column_letter  # Obtém a letra da coluna

    for cell in col:
      max_length = max(max_length, len(str(cell.value)))

    adjusted_width = (max_length + 2) * 1.2  # Ajuste para margem
    sheet.column_dimensions[col_letter].width = adjusted_width

  workbook.save(arquivo_excel)


def get_crashes(df, reverse, lines=300, day_limit=20):
  year, month = 0, 0
  df_grouped = pd.DataFrame(columns=df.columns)

  if reverse:
    year = df["CRASH_DATE"].dt.year.max()
    month = df[df["CRASH_DATE"].dt.year == year]["CRASH_DATE"].dt.month.max()
  else:
    year = df["CRASH_DATE"].dt.year.min()
    month = df[df["CRASH_DATE"].dt.year == year]["CRASH_DATE"].dt.month.min()

  while len(df_grouped) < lines:
    df_month = df[
      (df["CRASH_DATE"].dt.year == year) & (df["CRASH_DATE"].dt.month == month)
    ]

    if not df_month.empty:
      df_limited_month = (
        df_month.groupby(df_month["CRASH_DATE"].dt.date)
        .apply(lambda x: x.head(day_limit))
        .reset_index(drop=True)
      )

      df_limited_month = df_limited_month.dropna(axis=1, how="all")
      if not df_limited_month.empty:
        df_grouped = pd.concat([df_grouped, df_limited_month]).head(lines)

    if reverse:
      if month == 1:
        month = 12
        year -= 1
      else:
        month -= 1
    else:
      if month == 12:
        month = 1
        year += 1
      else:
        month += 1

  return df_grouped.sort_values(by="CRASH_DATE").reset_index(drop=True)


def reduce_data(csv_file, xlsx_file, lines=300, day_limit=10) -> None:
  df = pd.read_csv(csv_file)

  df["CRASH_DATE"] = pd.to_datetime(
    df["CRASH_DATE"], format="%m/%d/%Y %I:%M:%S %p", errors="coerce"
  )

  df = df.sort_values(by="CRASH_DATE").reset_index(drop=True)
  get_crashes(df=df, reverse=False, lines=lines, day_limit=day_limit).to_excel(
    xlsx_file, index=False
  )
  resize_columns(xlsx_file)
