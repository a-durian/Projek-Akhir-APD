from datetime import datetime, timedelta
from register_akun import register

# untuk menghindari circular imports.
# importnya dipindahin ke baris dan program yg membtuhkan importnya (Lazy Imports)
import questionary as qs

history_pesanan = {}
akun = {"admin": ["admin123", "admin"]}
daftar_pesanan = {}
daftar_barang = {
     1: {"nama": "Roti Tawar", "harga": 12000},
     2: {"nama": "Konohamie Mi Instan Goreng", "harga": 3200},
     3: {"nama": "Konohamie Mi Instan Kari Ayam", "harga": 3200},
     4: {"nama": "Geng-Geng Wafer Chocolate", "harga": 9900},
     5: {"nama": "Silver King", "harga": 25000},
     6: {"nama": "Lolari Sweat", "harga": 8000},
     7: {"nama": "Bad Day", "harga": 13000},
     8: {"nama": "Konohamilk", "harga": 14000},
     9: {"nama": "Youzone", "harga": 16000},
     10: {"nama": "Beras 5KG", "harga": 77000}
} #nomor..: {nama:, harga:}
keranjang_belanja = {}
riwayat_transaksi = {}
waktu_pembelian = []
waktu_sampai = []

if __name__ == "__main__":
    while True:
        # regist
        username = register(akun)
        hak_akun = akun[username][1]

        match hak_akun:

            # user program
            case "user":
                while True:
                    pilihan = qs.select(
                        "Selamat Datang Di Toko Kami '-' ",
                        ["Pesan Barang", "Status Pesanan", "History Pesanan", "Keluar"],
                    ).ask()

                    match pilihan:
                        case "Pesan Barang":
                            # import pembelian disini untuk menghindari circular import
                            from tambah_ke_keranjang import Tambah_Barang_ke_Keranjang as pembelian
                            pembelian(
                                daftar_pesanan,
                                daftar_barang,
                                waktu_pembelian,
                                waktu_sampai,
                                username,
                            )
                            continue

                        case "Status Pesanan":
                            from status_pesanan import status
                            status(
                                daftar_pesanan,
                                waktu_sampai,
                                waktu_pembelian,
                                history_pesanan,
                            )
                            continue

                        case "History Pesanan":
                            from history_pembelian import history
                            history(history_pesanan)
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
            case "Keluar":
                break
