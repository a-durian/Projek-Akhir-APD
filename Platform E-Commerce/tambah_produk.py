import questionary as qs
import variabel_global as var
from lihat_daftar_barang import listProduk


def tambah_barang():
    listProduk()
    print("\nSilahkan input nama, harga dan stok barang...\n")
    nama = qs.text("Nama barang:").ask()
    harga = qs.text("Harga barang:").ask()
    stock = qs.text("Stok barang:").ask()
    if nama == "":
        print("\n!! Input Tidak Boleh Kosong !!\n")
        return
    if not (harga) or not (harga.isdigit()) or int(harga) <= 0:
        print("\n!! Input Tidak Valid !!\n")
        return
    if not (stock) or not (stock.isdigit()) or int(stock) <= 0:
        print("\n!! Input Tidak Valid !!\n")
        return
    for barang in var.daftar_barang.values():
        if barang["nama"].lower() == nama.lower():
            print("\n !! Barang sudah ada !!\n")
            return
    konfirmasi = qs.confirm(
        f"Tambahkan '{nama}' (Harga: {harga}, Stok: {stock})?"
    ).ask()
    if not konfirmasi:
        print("\n ! Penambahan dibatalkan. !\n")
        return
    var.daftar_barang[len(var.daftar_barang.keys()) + 1] = {
        "nama": nama,
        "harga": int(harga),
        "stock": int(stock),
    }
    print("\n + Barang berhasil ditambahkan! \n")
