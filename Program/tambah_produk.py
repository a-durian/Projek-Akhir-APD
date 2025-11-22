import questionary as qs
import variabel_global as var


def tambah_barang():
    print("\n=== Tambah Barang ===")
    nama = qs.text("Nama barang:").ask()
    harga = qs.text("Harga barang:").ask()
    stock = qs.text("Stok barang:").ask()
    if nama == "":
        print("Nama Produk Tidak Boleh Kosong")
        return
    if not (harga) or not (harga.isdigit()) or int(harga) <= 0:
        print("Harga Tidak Valid")
        return
    if not (stock) or not (stock.isdigit()) or int(stock) <= 0:
        print("Stock Tidak Valid")
        return
    for barang in var.daftar_barang.values():
        if barang["nama"].lower() == nama.lower():
            print("Barang sudah ada!")
            return
    konfirmasi = qs.confirm(
        f"Tambahkan '{nama}' (Harga: {harga}, Stok: {stock})?"
    ).ask()
    if not konfirmasi:
        print("Penambahan dibatalkan.")
        return
    var.daftar_barang[len(var.daftar_barang.keys()) + 1] = {
        "nama": nama,
        "harga": int(harga),
        "stock": int(stock),
    }
    print("Barang berhasil ditambahkan!")
