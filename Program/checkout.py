from prettytable import PrettyTable
from datetime import datetime, timedelta, timezone as timedate
import random, sys, questionary as qs
from copy import deepcopy
import variabel_global as var
from fungsi import clear_terminal
from tambah_ke_keranjang import Tambah_Barang_ke_Keranjang

# Untuk menghindari overwrite data lama terhadap data baru, import variabel_global, jangan pakai from variabel_global karena hanya akan menjadi referensi bukan merujuk ke variabel asli


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
    # deklarasi tabel_keranjang sebagai objek PrettyTable
    tabel_keranjang = PrettyTable()
    tabel_keranjang.field_names = ["No", "Nama Produk", "Jumlah", "Subtotal"]
    print("")
    tabel_keranjang.align["Nama Produk"] = "l"
    tabel_keranjang.align["Subtotal"] = "l"
    # import shared data lazily

    if not var.keranjang_belanja:
        print("Keranjang belanja kosong.")
        # kembaliKeMenu(menuCustomer)
        # #setelah ini seharusnya akan kembali ke menu user
    else:
        total = 0
        for id, barang in enumerate(var.keranjang_belanja[username].values(), start=1):
            print(barang)
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


def Lanjut_Pembayaran(username):
    # kalau tidak ada produk di keranjang belanja
    # import shared state lazily
    if var.keranjang_belanja[username]:
        try:
            not var.keranjang_belanja[username]
        except ValueError:
            print("Keranjang belanja kosong.")
            # kembaliKeMenu(menuCustomer)
            pass

        opsi_lanjut = qs.confirm("Apakah Anda ingin melakukan pembayaran?").ask()
        if opsi_lanjut == True:
            print(
                "\nBerhasil melakukan pembelian! Terima kasih telah berbelanja di KlikCodemaret.\n"
            )
            # Simpan snapshot keranjang beserta waktu transaksi
            key_akhir = len(var.riwayat_transaksi[username]) + 1
            var.riwayat_transaksi[username][key_akhir] = {
                "waktu_pembelian": datetime.now(),
                "barang": deepcopy(var.keranjang_belanja[username]),
                "waktu_estimasi": datetime.now()
                + timedelta(minutes=random.choice([1, 2, 3])),
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
        print("Belum Ada Produk Di Keranjang Belanja")


def hapus_Produk_Keranjang(username):
    daftar_Keranjang_Belanja(username)
    salinan_keranjang_belanja = deepcopy(var.keranjang_belanja)
    key_akhir = len(var.keranjang_belanja[username].keys())
    pilihan_hapus = qs.text("Masukan Id Barang Yang Di Hapus : ").ask()
    if (
        pilihan_hapus.isdigit()
        and int(pilihan_hapus) >= 1
        or int(pilihan_hapus) <= key_akhir
    ):
        for id, barang in var.keranjang_belanja[username].items():
            for i in range(int(pilihan_hapus), key_akhir):
                salinan_keranjang_belanja[username][i] = barang
            del salinan_keranjang_belanja[username][key_akhir]
        var.keranjang_belanja[username] = deepcopy(salinan_keranjang_belanja[username])
    else:
        print("Input Tidak Valid")
