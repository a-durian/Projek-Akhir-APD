import questionary as qs
from lihat_daftar_barang import listProduk
import variabel_global as var
from copy import deepcopy


def Tambah_Barang_ke_Keranjang(username):
    if var.daftar_barang:
        # "import lazily" untuk menghindari circular imports
        listProduk()
        print("\nMasukkan [0] untuk kembali ke menu awal\n")
        menu_grosir_input = qs.text(
            "Silahkan pilih nomor produk untuk dimasukkan ke keranjang belanja: "
        ).ask()
        if menu_grosir_input.isdigit():
            menu_grosir = int(menu_grosir_input)
            if menu_grosir == 0:
                print("\nKembali ke menu awal...\n")
                # menuCustomer() #>> Hharusnya disini kembali ke menu customer
                pass
            elif menu_grosir in var.daftar_barang:
                jumlah_input = input("Masukkan jumlah [1/2/...]: ")
                if jumlah_input == "":
                    jumlah = 1
                elif (
                    jumlah_input.isdigit()
                    and int(jumlah_input) > 0
                    and not (
                        var.daftar_barang[menu_grosir]["stock"] - int(jumlah_input)
                    )
                    < 0
                ):
                    jumlah = int(jumlah_input)
                else:
                    print("\n!! Jumlah tidak valid. Silahkan coba lagi.!!\n")
                    Tambah_Barang_ke_Keranjang(username)
                var.keranjang_belanja[username][
                    len(var.keranjang_belanja[username]) + 1
                ] = {
                    "nama": var.daftar_barang[menu_grosir]["nama"],
                    "harga": var.daftar_barang[menu_grosir]["harga"]
                    - (var.daftar_barang[menu_grosir]["harga"] * var.diskon),
                    "jumlah": jumlah,
                }

                nama = var.daftar_barang[menu_grosir]["nama"]
                harga = var.daftar_barang[menu_grosir]["harga"]
                var.daftar_barang[menu_grosir]["stock"] -= jumlah
                # menghapus barang yang stock nya sudah habis dari daftar_barang
                key_akhir = len(var.daftar_barang.keys())
                salinan_daftar_barang = deepcopy(var.daftar_barang)
                for id, info_barang in var.daftar_barang.items():
                    if info_barang["stock"] == 0:
                        for i in range(id, key_akhir):
                            salinan_daftar_barang[i] = deepcopy(
                                salinan_daftar_barang[i + 1]
                            )
                        del salinan_daftar_barang[key_akhir]
                var.daftar_barang = deepcopy(salinan_daftar_barang)

                print(
                    f"\n+ {nama} x{jumlah} seharga Rp.{harga:,} berhasil ditambahkan ke keranjang belanja.\n"
                )

                # opsiLagi(menuCustomer, "Checkout produk lagi?", Tambah_Barang_ke_Keranjang)
                # ^^ disini harusnya ada output nanya ntuk coba lagi...
                pass
            else:
                print("\nProduk tidak ditemukan. Silahkan coba lagi.\n")
                Tambah_Barang_ke_Keranjang(username)
        else:
            print("\n!! Input harus berupa nomor. Silahkan coba lagi. !!\n")
            Tambah_Barang_ke_Keranjang(username)
    else:
        print("Belum Ada Produk")


if __name__ == "__main__":
    pass
