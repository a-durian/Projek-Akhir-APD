from prettytable import PrettyTable
import variabel_global as var


# ///Tampilkan daftar produk dari dictionary `Produk`.///
def listProduk():
    if var.daftar_barang:
        tabel = PrettyTable()
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
        print("Belum Ada Produk")
        return
