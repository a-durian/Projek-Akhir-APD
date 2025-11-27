from prettytable import PrettyTable, TableStyle
import pandas as pd
import csv
import matplotlib.pyplot as plt


def list_data_pemasukan():
    try:

        with open("data_pemasukan.csv", mode="r") as file:
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

        df = pd.read_csv("data_pemasukan.csv")
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

    except KeyError:
        print("\n! Belum ada data pemasukan !\n")
