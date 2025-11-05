from prettytable import PrettyTable
import questionary, cursor, time, os
from datetime import datetime


"""print(datetime.now())

table = PrettyTable()
test = ["Nama", "Harga", "Stock"]
table.field_names = test
table.add_row(["Kecap", "20.000", "12"])
print(table)

pilihan_barang = questionary.checkbox(
    "Pilih Barang Belanja", choices=["Kecap", "Saus", "Kue Abon"]
).ask()

while True:
    masukan = input("Tekan Enter")
    if masukan == "":
        waktu_sebelum = time.time()
        print(f"Waktu Sekarang\t: {waktu_sebelum}")
    else:
        print("Masukan Salah")
        lanjut = input("Lanjut ? ")
        if lanjut.lower() == "y":
            continue
        else:
            break
    waktu_sekarang = time.time()
    print(f"Waktu Sekarang\t: {waktu_sekarang}")
    print(f"Selisih Waktu\t: {waktu_sekarang - waktu_sebelum}")
"""
# Jam Digital
while True:
    os.system("clear")
    tabel = PrettyTable()
    waktu_sekarang = [datetime.now().strftime("%H:%M:%S")]
    tabel.field_names = waktu_sekarang
    print(tabel)
    time.sleep(1)

print("Program Selesai")
