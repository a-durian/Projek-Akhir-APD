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
from fungsi import clear_terminal, Loading
from kelola_user import Kelola_user
from lihat_data_pemasukan import list_data_pemasukan
import time
import questionary as qs
import variabel_global as var

if __name__ == "__main__":

    Loading()
    while True:

        # regist
        reg = register()
        hak_akun = reg.get("hak")
        username = reg.get("username")

        match hak_akun:
            # user program
            case "user":
                while True:
                    if var.diskon > 0:
                        print(
                            f"Hari ini terdapat diskon sebesar: {int(var.diskon*100)}%!\n"
                        )
                    pilihan = qs.select(
                        f"Halo {username} Selamat Datang Di KlikCode Grosir. Silahkan pilih menu: ",
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
                        "Selamat Datang Admin. Silahkan pilih menu: ",
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
                            list_data_pemasukan()
                        case "Tambahkan Diskon Barang":
                            diskon()
                        case "Kelola Akun User":
                            Kelola_user()
                        case "Keluar":
                            break
