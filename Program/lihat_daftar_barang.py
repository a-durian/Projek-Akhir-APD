from prettytable import PrettyTable


# ///Tampilkan daftar produk dari dictionary `Produk`.///
def listProduk():
    # import daftar_barang lazily to avoid circular imports
    from main import daftar_barang

    # variabel tabel sebagai objek PrettyTable
    tabel = PrettyTable()

    # Membersihkan isi tabel sebelumnya supaya tidak terjadi duplikasi saat dipanggil berulang.
    tabel.clear_rows()  # bersihkan baris lama pada objek tabel
    tabel.field_names = ["No", "Nama Produk", "Harga"]
    tabel.align["Nama Produk"] = "l"
    tabel.align["Harga"] = "l"
    for i, produk in daftar_barang.items():  # tambahkan setiap produk ke tabel
        tabel.add_row([i, produk["nama"], f"Rp.{produk['harga']:,}"])
    # for i, (key, produk) in enumerate(daftar_barang.items(), 1):  # tambahkan setiap produk ke tabel
    #     nama = produk.get("nama", str(key))
    #     harga = produk.get("harga", 0)
    #     tabel.add_row([i, nama, f"Rp.{harga:,}"])
    print(tabel)


if __name__ == "__main__":
    listProduk()
