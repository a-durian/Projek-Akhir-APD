import variabel_global as var
import questionary as qs
from lihat_daftar_barang import listProduk


def diskon():
    try:
        diskon = float(qs.text("Berapa Persen Diskon 1-100 : ").ask())
        if diskon < 1 or diskon > 100:
            raise ValueError("Input Diskon Diluar Batas")
        var.diskon = diskon * 0.01
    except ValueError:
        print("Input Tidak Valid")
        return
