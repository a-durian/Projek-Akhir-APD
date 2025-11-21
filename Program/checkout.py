import questionary as qs
from prettytable import PrettyTable
from datetime import datetime, timedelta, timezone as timedate
import random, sys
from copy import deepcopy
from main import riwayat_transaksi, keranjang_belanja

# Untuk menghindari circular imports.
# import: (keranjang_belanja, daftar_barang, riwayat_transaksi)
# dipindahkan didalam fungsi yang akan berjalan hanya ketika dibutuhkan.


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
            daftar_Keranjang_Belanja(username)
        case "Lanjut ke Pembayaran":
            Lanjut_Pembayaran(username)
        case "Tambah Barang ke Keranjang":
            from tambah_ke_keranjang import Tambah_Barang_ke_Keranjang

            Tambah_Barang_ke_Keranjang(username)
        case "Hapus Barang dari Keranjang":
            hapus_Produk_Keranjang()  # fungsi untuk menghapus barang dari keranjang
            pass
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
    from main import keranjang_belanja

    if not keranjang_belanja:
        print("Keranjang belanja kosong.")
        # kembaliKeMenu(menuCustomer)
        # #setelah ini seharusnya akan kembali ke menu user
    else:
        total = 0
        for id, barang in enumerate(keranjang_belanja[username].values(), start=1):
            print(barang)
            nama = barang["nama"]
            harga = barang["harga"]
            jumlah = barang["jumlah"]
            subtotal = harga * jumlah
            total += subtotal
            tabel_keranjang.add_row([id, nama, jumlah, f"Rp.{subtotal:,}"])
        tabel_keranjang.add_row(["", "", "", ""])
        tabel_keranjang.add_row(["", "", "Total:", f"Rp.{total:,}"])
        print(tabel_keranjang)
        menu_Keranjang(username)
        # kembali  ke menu keranjang belanja


def Lanjut_Pembayaran(username):
    # kalau tidak ada produk di keranjang belanja
    # import shared state lazily

    try:
        not keranjang_belanja[username]
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
        key_akhir = len(riwayat_transaksi[username]) + 1
        riwayat_transaksi[username][key_akhir] = {
            "waktu_pembelian": datetime.now(),
            "barang": deepcopy(keranjang_belanja[username]),
            "waktu_estimasi": datetime.now()
            + timedelta(minutes=random.choice([1, 2, 3])),
        }
        keranjang_belanja[username].clear()
        print(riwayat_transaksi)
        print("Kembali ke menu customer...\n")
        # disini seharusnya kembali ke menu customer
    elif opsi_lanjut == False:
        print("\nTransaksi dibatalkan. Kembali ke menu customer...\n")
    else:
        print("\n!! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi. !!\n")
        return Lanjut_Pembayaran(username)


def hapus_Produk_Keranjang():
    tabel_hapus = PrettyTable()
    # DEKLARASI tabelHapus_dariKeranjang
    tabelHapus_dariKeranjang = PrettyTable()
    print("\nHapus produk dari keranjang belanja...\n")
    from main import keranjang_belanja, daftar_barang

    if not keranjang_belanja:  # Cek apakah keranjang belanja kosong
        print("Keranjang belanja kosong.")
        # kembaliKeMenu(menuCustomer) #kembali ke menu user
        pass
    else:  # Jika tidak kosong, tampilkan isi keranjang belanja
        items = list(keranjang_belanja.items())
        for no_id, (id_produk, jumlah) in enumerate(items, 1):
            nama = daftar_barang[id_produk]["nama"]
            harga = daftar_barang[id_produk]["harga"]
            # Prettytable tabelHapus_dariKeranjang
            tabelHapus_dariKeranjang.field_names = [
                "No",
                "Nama Produk",
                "Jumlah",
                "Harga",
            ]
            tabelHapus_dariKeranjang.add_row(
                [no_id, nama, jumlah, f"Rp.{harga * jumlah:,}"]
            )
        tabelHapus_dariKeranjang.align["Nama Produk"] = "l"
        tabelHapus_dariKeranjang.align["Harga"] = "l"
        print(tabelHapus_dariKeranjang)
        hapus_produk = input("\nMasukkan nomor produk yang ingin dihapus: ")
        if hapus_produk.isdigit():
            hapus_noId = int(hapus_produk)
            if 1 <= hapus_noId <= len(items):
                id_produk_to_remove = items[hapus_noId - 1][0]
                del keranjang_belanja[id_produk_to_remove]
                print("\n- Produk berhasil dihapus dari keranjang belanja.")
                # opsiLagi(menu_keranjang, "Hapus produk lagi dari keranjang?", opsiHapusDariKeranjang)
                # disini harusnya ada output nanya ntuk coba lagi...
                pass
            else:
                print("\n!! Nomor produk tidak valid. Silahkan coba lagi. !!\n")
                return hapus_Produk_Keranjang()
        else:
            print("\n! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi.\n")
            return hapus_Produk_Keranjang()
