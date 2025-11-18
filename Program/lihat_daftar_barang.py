from prettytable import PrettyTable
from main import daftar_barang

# variabel tabel sebagai objek PrettyTable
tabel = PrettyTable()


# ///Tampilkan daftar produk dari dictionary `Produk`.///
def listProduk():
    # Membersihkan isi tabel sebelumnya supaya tidak terjadi duplikasi saat dipanggil berulang.
    tabel.clear_rows()  # bersihkan baris lama pada objek tabel
    tabel.field_names = ["No", "Nama Produk", "Harga"]
    tabel.align["Nama Produk"] = "l"
    tabel.align["Harga"] = "l"
    for i, produk in daftar_barang.items():  # tambahkan setiap produk ke tabel
        tabel.add_row([i, produk["nama"], f"Rp.{produk['harga']:,}"])
    print(tabel)


if __name__ == "__main__":
    listProduk()
