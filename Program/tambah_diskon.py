import variabel_global as var
import questionary as qs
from lihat_daftar_barang import listProduk


def diskon():
    pilihan = qs.select(
        "Pilih Jenis Diskon", ["Diskon Barang", "Diskon Pembelian"]
    ).ask()
    match pilihan:
        case "Diskon Barang":
            pass
        case "Diskon Pembelian":
            try:
                diskon = float(qs.text("Berapa Persen Diskon 1-100 : ").ask())
                if diskon < 1 or diskon > 100:
                    raise ValueError("Input Diskon Diluar Batas")
                var.diskon = diskon * 0.01
            except ValueError:
                print("Masukan Harusa Berupa Angka")
                return
