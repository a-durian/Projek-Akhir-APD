from datetime import datetime, timedelta
from status_pesanan import status
from register_akun import register
from tambah_produk import tambah_barang
from lihat_daftar_barang import listProduk
from update_produk import update_barang
from hapus_produk import hapusProduk
from checkout import menu_Keranjang
from history_pembelian import history
from tambah_diskon import diskon
from fungsi import clear_terminal
import time
import questionary as qs
import variabel_global as var

if __name__ == "__main__":
    while True:
        # animasi loading
        loading = ["l", "o", "a", "d", "i", "n", "g"]
        batas = 0
        while batas <= 3:
            for i in loading:
                print(f"{i}", end="", flush=True)
                time.sleep(0.1)
            clear_terminal()
            batas += 1

        # regist
        reg = register()
        hak_akun = reg[1]
        username = reg[0]

        match hak_akun:

            # user program
            case "user":
                while True:
                    pilihan = qs.select(
                        "Selamat Datang Di Toko Kami '-' ",
                        [
                            "Keranjang Belanja",
                            "Status Pesanan",
                            "History Pesanan",
                            "Keluar",
                        ],
                    ).ask()
                    match pilihan:
                        case "Keranjang Belanja":
                            menu_Keranjang(username)
                            continue

                        case "Status Pesanan":
                            status(username)
                            continue

                        case "History Pesanan":
                            history(username)
                            continue

                        case "Keluar":
                            break
            # admin program
            case "admin":
                while True:
                    pilihan = qs.select(
                        "Selamat Datang Admin '-'",
                        [
                            "Tambah Daftar Barang",
                            "Tampilkan Daftar Barang",
                            "Update Daftar Barang",
                            "Hapus Daftar Barang",
                            "Tampilkan Data Penjualan",
                            "Tambahkan Diskon Barang",
                            "Kelola Akun User",
                            "Keluar",
                        ],
                    ).ask()
                    match pilihan:
                        case "Tambah Daftar Barang":
                            tambah_barang()
                        case "Tampilkan Daftar Barang":
                            listProduk()
                        case "Update Daftar Barang":
                            update_barang()
                        case "Hapus Daftar Barang":
                            hapusProduk()
                        case "Tampilkan Data Penjualan":
                            pass
                        case "Tambahkan Diskon Barang":
                            diskon()
                        case "Kelola Akun User":
                            pass
                        case "Keluar":
                            break
