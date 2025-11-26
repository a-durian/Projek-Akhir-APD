from prettytable import PrettyTable, TableStyle
import pandas as pd
import csv
import matplotlib.pyplot as plt

NAMA_FILE_PEMASUKAN = "data_pemasukan.csv"


def list_data_pemasukan():
    try:
        df = pd.read_csv(NAMA_FILE_PEMASUKAN)
        df["Tanggal"] = pd.to_datetime(df["Tanggal"])
        df["Total"] = df["Harga"] + df["Jumlah"]
        df_per_hari = df.groupby(df["Tanggal"].dt.date)["Total"].sum()
        x = df_per_hari.index
        y = df_per_hari.values
        plt.figure(figsize=(10, 5))
        plt.plot(x, y, marker="o")
        plt.xlabel("Tanggal")
        plt.ylabel("Total Pemasukan")
        plt.title("Total Pemasukan Per Hari")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        with open(NAMA_FILE_PEMASUKAN, mode="r") as file:
            reader = csv.reader(file)
            table = PrettyTable()
            table.set_style(TableStyle.SINGLE_BORDER)
            header = next(reader, None)
            if header:
                table.field_names = header

            for row in reader:
                table.add_row(row)

            table.align["Nama Produk"] = "l"
            table.align["Harga"] = "l"

            print("\n=== Daftar Data Pemasukan ===")
            print(table)
    except FileNotFoundError:
        print("\n! Belum ada data pemasukan !\n")
