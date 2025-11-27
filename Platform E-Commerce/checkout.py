from prettytable import PrettyTable, TableStyle
from datetime import datetime, timedelta, timezone as timedate
import random, sys, questionary as qs
from copy import deepcopy
import variabel_global as var
from fungsi import clear_terminal
from colorama import init, Fore, Style
from lihat_daftar_barang import listProduk

init(
    autoreset=True
)  # >>Untuk menghindari overwrite data lama terhadap data baru, import variabel_global, jangan pakai from variabel_global karena hanya akan menjadi referensi bukan merujuk ke variabel asli


def menu_Keranjang(username):
    pilihan = qs.select(
        "Menu Keranjang Belanja:",
        choices=[
            "Lihat Daftar Keranjang Belanja",
            "Lanjut ke Pembayaran",
            "Tambah Barang ke Keranjang",
            "Hapus Barang dari Keranjang",
            "Kembali ke Menu Utama",
        ],
    ).ask()

    match pilihan:
        case "Lihat Daftar Keranjang Belanja":
            clear_terminal()
            daftar_Keranjang_Belanja(username)
        case "Lanjut ke Pembayaran":
            clear_terminal()
            Lanjut_Pembayaran(username)
        case "Tambah Barang ke Keranjang":
            clear_terminal()
            Tambah_Barang_ke_Keranjang(username)
        case "Hapus Barang dari Keranjang":
            clear_terminal()
            hapus_Produk_Keranjang(username)
        case "Kembali ke Menu Utama User":
            sys.exit()


def daftar_Keranjang_Belanja(username):
    if var.keranjang_belanja[username]:
        tabel_keranjang = (
            PrettyTable()
        )  # deklarasi tabel_keranjang sebagai objek PrettyTable
        tabel_keranjang.set_style(TableStyle.SINGLE_BORDER)
        tabel_keranjang.field_names = ["No", "Nama Produk", "Jumlah", "Subtotal"]
        print("")
        tabel_keranjang.align["Nama Produk"] = "l"
        tabel_keranjang.align["Harga"] = "l"
        tabel_keranjang.align["Subtotal"] = "l"
        total = 0
        for id, barang in enumerate(var.keranjang_belanja[username].values(), start=1):
            nama = barang["nama"]
            harga = barang["harga"]
            jumlah = barang["jumlah"]
            subtotal = harga * jumlah
            total += subtotal
            tabel_keranjang.add_row([id, nama, jumlah, f"Rp.{subtotal:,}"])
        tabel_keranjang.add_row(["", "", "", ""])
        tabel_keranjang.add_row(["", "", "Total:", f"Rp.{total:,}".replace(",", ".")])
        print(tabel_keranjang)
        # kembali  ke menu keranjang belanja
    else:
        print("\n!! Belum Ada Produk Di Keranjang Belanja !!\n")
        # kembali ke menu sebelumnya


def Lanjut_Pembayaran(username):
    if var.keranjang_belanja[username]:
        daftar_Keranjang_Belanja(username)
        opsi_lanjut = qs.confirm("Apakah Anda ingin melakukan pembayaran?").ask()
        if opsi_lanjut == True:
            print(
                "\nBerhasil melakukan pembelian! Terima kasih telah berbelanja di KlikCodemaret.\n"
            )
            # Simpan snapshot keranjang beserta waktu transaksi
            key_akhir = len(var.riwayat_transaksi[username]) + 1
            var.riwayat_transaksi[username][key_akhir] = {
                "waktu_pembelian": datetime.now().replace(microsecond=0),
                "barang": deepcopy(var.keranjang_belanja[username]),
                "waktu_estimasi": datetime.now().replace(microsecond=0)
                + timedelta(seconds=random.choice([15, 20])),
            }
            var.keranjang_belanja[username].clear()
            print("Kembali ke menu customer...\n")
            # disini seharusnya kembali ke menu customer
        elif opsi_lanjut == False:
            print("\nTransaksi dibatalkan. Kembali ke menu customer...\n")
        else:
            print("\n!! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi. !!\n")
            return Lanjut_Pembayaran(username)
    else:
        print("\n!! Belum Ada Produk Di Keranjang Belanja !!\n")


def Tambah_Barang_ke_Keranjang(username):
    if var.daftar_barang:
        listProduk()
        menu_grosir_input = qs.text(
            "Masukkan [0] untuk kembali ke menu awal\n  Silahkan pilih nomor produk untuk dimasukkan ke keranjang belanja: "
        ).ask()
        if menu_grosir_input.isdigit():
            menu_grosir = int(menu_grosir_input)
            if menu_grosir == 0:
                print("\nKembali ke menu awal...\n")
                pass
            elif menu_grosir in var.daftar_barang:
                jumlah_input = qs.text("Selanjutnya masukkan jumlah [1/2/...]: ").ask()
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
                    return
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
                # ^^ disini harusnya ada output nanya ntuk coba lagi...
                pass
            else:
                print("\n!! Produk tidak ditemukan. Silahkan coba lagi. !!\n")
                Tambah_Barang_ke_Keranjang(username)
        else:
            print("\n!! Input harus berupa nomor. Silahkan coba lagi. !!\n")
            Tambah_Barang_ke_Keranjang(username)
    else:
        print("\n! Belum Ada Produk !\n")


if __name__ == "__main__":
    pass


def hapus_Produk_Keranjang(username):
    if var.keranjang_belanja[username]:
        daftar_Keranjang_Belanja(username)
        salinan_keranjang_belanja = deepcopy(var.keranjang_belanja)
        key_akhir = len(var.keranjang_belanja[username].keys())
        pilihan_hapus = qs.text("Masukan Id Barang Yang Di Hapus : ").ask()
        if (
            pilihan_hapus.isdigit()
            and int(pilihan_hapus) >= 1
            and int(pilihan_hapus) <= key_akhir
        ):
            for id in range(int(pilihan_hapus), key_akhir):
                if id < key_akhir:
                    salinan_keranjang_belanja[username][id] = salinan_keranjang_belanja[username][id + 1]
            del salinan_keranjang_belanja[username][key_akhir]
            var.keranjang_belanja[username] = deepcopy(
                salinan_keranjang_belanja[username]
            )
            print("\n- Barang berhasil dihapus dari keranjang belanja.\n")
        else:
            print("\n!! Input Tidak Valid. Silahkan coba lagi. !!\n")
            hapus_Produk_Keranjang(username)
    else:
        print("\n ! Keranjang Belanja Mu Masih Kosong !\n")
        return

