import questionary as qs
from copy import deepcopy
from lihat_daftar_barang import listProduk
import variabel_global as var


def hapusProduk():

    listProduk()
    try:
        pilihan_id = int(qs.text("Masukan Id Barang Yang Ingin Di Hapus : ").ask())
        if pilihan_id in var.daftar_barang.keys():
            salinan_daftar_barang = deepcopy(var.daftar_barang)
            key_akhir = len(var.daftar_barang.keys())
            for batas in range(pilihan_id, key_akhir):
                if pilihan_id < key_akhir:
                    salinan_daftar_barang[batas] = salinan_daftar_barang[batas + 1]
                    continue
            del salinan_daftar_barang[key_akhir]
            print("\n+ Hapus Barang Berhasil!\n")
            var.daftar_barang = deepcopy(salinan_daftar_barang)
    except ValueError:
        print("\n!! Pilihan Tidak Valid !!\n")
        return
