import prettytable as PrettyTable
import questionary as qs
from lihat_daftar_barang import listProduk
from main import daftar_barang, keranjang_belanja
from checkout import daftar_Keranjang_Belanja


def Tambah_Barang_ke_Keranjang(username):
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
        elif menu_grosir in daftar_barang:
            jumlah_input = input("Masukkan jumlah [1/2/...]: ")
            if jumlah_input == "":
                jumlah = 1
            elif (
                jumlah_input.isdigit()
                and int(jumlah_input) > 0
                and not (daftar_barang[menu_grosir]["stock"] - int(jumlah_input)) < 0
            ):
                jumlah = int(jumlah_input)
            else:
                print("\n!! Jumlah tidak valid. Silahkan coba lagi.!!\n")
                Tambah_Barang_ke_Keranjang()
            keranjang_belanja[username][len(keranjang_belanja[username]) + 1] = {
                "nama": daftar_barang[menu_grosir]["nama"],
                "harga": daftar_barang[menu_grosir]["harga"],
                "jumlah": jumlah,
            }

            nama = daftar_barang[menu_grosir]["nama"]
            harga = daftar_barang[menu_grosir]["harga"]
            daftar_barang[menu_grosir]["stock"] -= jumlah
            # menghapus barang yang stock nya sudah habis dari daftar_barang
            total_delete = 0
            key_akhir = len(daftar_barang.keys())
            batas = menu_grosir
            for id, info_barang in daftar_barang.items():
                if info_barang["stock"] == 0:
                    if id >= 1 and id != key_akhir:
                        for i in range(id, key_akhir + 1):
                            if i <= key_akhir - 1:
                                if i + 1 <= key_akhir:
                                    daftar_barang[i] = daftar_barang[i + 1]

            del daftar_barang[key_akhir]

            print(daftar_barang)
            print(
                f"\n+ {nama} x{jumlah} seharga Rp.{harga:,} berhasil ditambahkan ke keranjang belanja.\n"
            )

            # opsiLagi(menuCustomer, "Checkout produk lagi?", Tambah_Barang_ke_Keranjang)
            # ^^ disini harusnya ada output nanya ntuk coba lagi...
            pass
        else:
            print("\nProduk tidak ditemukan. Silahkan coba lagi.\n")
            Tambah_Barang_ke_Keranjang()
    else:
        print("\n!! Input harus berupa nomor. Silahkan coba lagi. !!\n")
        Tambah_Barang_ke_Keranjang()


if __name__ == "__main__":
    pass
