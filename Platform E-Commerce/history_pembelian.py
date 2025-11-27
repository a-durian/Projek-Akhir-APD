from prettytable import PrettyTable, TableStyle
import variabel_global as var


def history(username):
    if var.history_pesanan[username]:
        for id in var.history_pesanan[username].values():
            tabel_history = PrettyTable()
            tabel_history.set_style(TableStyle.SINGLE_BORDER)
            tabel_history.field_names = ["No", "Nama Produk", "Jumlah", "Harga"]
            tabel_history.align["Harga"] = "l"
            tabel_history.align["Nama Produk"] = "l"
            total = 0
            for idbarang, barang in id["barang"].items():
                tabel_history.add_row(
                    [
                        idbarang,
                        barang["nama"],
                        barang["jumlah"],
                        f"Rp.{barang["harga"]:,}",
                    ]
                )
                total += barang["harga"] * barang["jumlah"]
            tabel_history.add_row(["", "", "", ""])
            tabel_history.add_row(["", "", "Total", f"Rp.{total:,}"])
            print(tabel_history)
            print(f"Pesanan Telah Diterima pada {id["waktu_estimasi"]}\n")

    else:
        print("\n! Kamu Belum Pernah Memesan Barang !\n")
