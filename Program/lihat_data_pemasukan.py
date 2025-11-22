from prettytable import PrettyTable
import pandas as pd
import csv

NAMA_FILE_PEMASUKAN = "data_pemasukan.csv"


def list_data_pemasukan():
    try:
        with open(NAMA_FILE_PEMASUKAN, mode="r") as file:
            reader = csv.reader(file)
            table = PrettyTable()

            header = next(reader, None)
            if header:
                table.field_names = header

            for row in reader:
                table.add_row(row)

            print("\n=== Daftar Data Pemasukan ===")
            print(table)

    except FileNotFoundError:
        print("Belum ada data pemasukan.")


list_data_pemasukan()

