import questionary as qs
from  prettytable import PrettyTable
from datetime import datetime, timedelta, timezone as timedate
import random
from main import keranjang_belanja, daftar_barang, riwayat_transaksi

def menu_Keranjang():
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

            daftar_Keranjang_Belanja()
        case "Lanjut ke Pembayaran":

            Lanjut_Pembayaran()
        case "Tambah Barang ke Keranjang":
            # fungsi untuk menambah barang ke keranjang
            pass
        case "Hapus Barang dari Keranjang":
            # fungsi untuk menghapus barang dari keranjang
            pass
        case "Kembali ke Menu Utama User":
            # fungsi untuk kembali ke menu utama user
            pass

def daftar_Keranjang_Belanja():
    # deklarasi tabel_keranjang sebagai objek PrettyTable
    tabel_keranjang = PrettyTable()
    tabel_keranjang.field_names = ["No", "Nama Produk", "Jumlah", "Subtotal"]
    print("")
    tabel_keranjang.align["Nama Produk"] = "l"
    tabel_keranjang.align["Subtotal"] = "l"
    if not keranjang_belanja:
        print("Keranjang belanja kosong.")
        # kembaliKeMenu(menuCustomer)
        # #setelah ini seharusnya akan kembali ke menu user
    else:
        total = 0
        for i, (product_id, jumlah) in enumerate(keranjang_belanja.items(), 1):
            nama = daftar_barang[product_id]["nama"]
            harga = daftar_barang[product_id]["harga"]
            subtotal = harga * jumlah
            total += subtotal
            tabel_keranjang.add_row([i, nama, jumlah, f"Rp.{subtotal:,}"])
        tabel_keranjang.add_row(["", "", "Total:", f"Rp.{total:,}"])
        print(tabel_keranjang)
        menu_Keranjang()
        # kembali  ke menu keranjang belanja
        
def Lanjut_Pembayaran():
    # kalau tidak ada produk di keranjang belanja
    try:
        not keranjang_belanja
    except ValueError:
        print("Keranjang belanja kosong.")
        # kembaliKeMenu(menuCustomer)
        pass

    opsi_lanjut = qs.confirm("Apakah Anda ingin melakukan pembayaran?").ask()
    if opsi_lanjut == True:
        print("\nBerhasil melakukan pembelian! Terima kasih telah berbelanja di KlikCodemaret.\n")
        # Simpan snapshot keranjang beserta waktu transaksi
        riwayat_transaksi.append(
            {
                "waktu_pembelian": datetime.now(),
                "items": keranjang_belanja.copy(),
                "waktu_estimasi": timedate.now() + timedelta(minutes=random.choice([1, 2, 3])),
            }
        )
        keranjang_belanja.clear()
        print("Kembali ke menu customer...\n")
        # return menuCustomer()\
        # disini seharusnya kembali ke menu customer
        pass
    elif opsi_lanjut == False:
        print("\nTransaksi dibatalkan. Kembali ke menu customer...\n")
        # return menuCustomer()
        # disini seharusnya kembali ke menu customer
        pass
    else:
        print("\n!! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi. !!\n")
        return Lanjut_Pembayaran()

def hapus_Produk_Keranjang():
    tabel_hapus = PrettyTable()
    # DEKLARASI tabelHapus_dariKeranjang
    tabelHapus_dariKeranjang = PrettyTable()
    print("\nHapus produk dari keranjang belanja...\n")
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
            tabelHapus_dariKeranjang.add_row([no_id, nama, jumlah, f"Rp.{harga * jumlah:,}"])
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
