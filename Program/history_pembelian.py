from prettytable import PrettyTable
import variabel_global as var


def history(username):
    if var.history_pembelian:
        tabel_history = PrettyTable()
        total = 0
        tabel_history.field_names = ["No", "Nama Produk", "Harga", "Jumlah"]
        for i in var.history_pesanan[username].values():
            for id, barang in enumerate(i["barang"].values(), start=1):
                tabel_history.add_row(
                    [id, barang["nama"], barang["harga"], barang["jumlah"]]
                )
                total += barang["jumlah"] * barang["harga"]
            tabel_history.add_row(["", "", "", ""])
            tabel_history.add_row(["", "", "Total", total])
            print(tabel_history)
            print(f"Pesanan Telah Di Terima Pada Waktu {i["waktu_estimasi"]}")
    else:
        print("Kamu Belum Pernah Memesan Barang")
