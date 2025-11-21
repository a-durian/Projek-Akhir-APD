from datetime import datetime, timedelta
from register_akun import register
import questionary as qs
from variabel_global import (
    history_pesanan,
    akun,
    daftar_barang,
    keranjang_belanja,
    riwayat_transaksi,
)

if __name__ == "__main__":
    while True:
        # regist
        hak_username = register(
            akun, keranjang_belanja, riwayat_transaksi, history_pesanan
        )
        hak_akun = hak_username[1]
        username = hak_username[0]

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
                            from checkout import menu_Keranjang

                            menu_Keranjang(username)
                            continue

                        case "Status Pesanan":
                            from status_pesanan import status

                            status(riwayat_transaksi, history_pesanan, username)
                            continue

                        case "History Pesanan":
                            from history_pembelian import history

                            history(history_pesanan, username)
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
                        ],
                    ).ask()
