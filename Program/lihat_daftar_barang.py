from prettytable import PrettyTable, TableStyle
import variabel_global as var


# ///Tampilkan daftar produk dari dictionary `Produk`.///
def listProduk():
    print(f"\n{'=== Daftar Barang ===':^60}")
    if var.daftar_barang:
        tabel = PrettyTable()
        tabel.set_style(TableStyle.SINGLE_BORDER)
        tabel.clear_rows()  # bersihkan baris lama pada objek tabel
        tabel.field_names = ["No", "Nama Produk", "Harga", "Stock"]
        tabel.align["Nama Produk"] = "l"
        tabel.align["Harga"] = "l"
        for i, produk in var.daftar_barang.items():  # tambahkan setiap produk ke tabel
            tabel.add_row(
                [
                    i,
                    produk["nama"],
                    f"Rp.{produk['harga']:,}".replace(",", "."),
                    produk["stock"],
                ]
            )
        print(tabel)
    else:
        print("\n! Belum Ada Produk !\n")
        return
