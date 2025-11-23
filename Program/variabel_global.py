from datetime import datetime, timedelta

diskon = 0.05
history_pesanan = {"a": {}}
akun = {
    1: {"username": "admin", "password": "admin123", "hak": "admin"},
    2: {"username": "a", "password": "a", "hak": "user"},
}
daftar_barang = {
    1: {"nama": "Roti Tawar", "harga": 12000, "stock": 2},
    2: {"nama": "Konohamie Mi Instan Goreng", "harga": 3200, "stock": 2},
    3: {"nama": "Konohamie Mi Instan Kari Ayam", "harga": 3200, "stock": 2},
    4: {"nama": "Geng-Geng Wafer Chocolate", "harga": 9900, "stock": 2},
    5: {"nama": "Silver King", "harga": 25000, "stock": 1},
    6: {"nama": "Lolari Sweat", "harga": 8000, "stock": 1},
    7: {"nama": "Bad Day", "harga": 13000, "stock": 4},
    8: {"nama": "Konohamilk", "harga": 14000, "stock": 3},
    9: {"nama": "Youzone", "harga": 16000, "stock": 2},
    10: {"nama": "Beras 5KG", "harga": 77000, "stock": 1},
}
keranjang_belanja = {"a": {1: {"nama": "Pop mie", "harga": 12009, "jumlah": 1}}}
riwayat_transaksi = {
    "a": {
        1: {
            "waktu_pembelian": datetime.now(),
            "barang": {
                1: {"nama": "tomat", "harga": 10090, "jumlah": 2},
            },
            "waktu_estimasi": datetime(2025, 11, 20, 12, 10, 00),
        },
    }
}
