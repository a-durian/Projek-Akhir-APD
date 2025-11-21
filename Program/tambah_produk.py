import questionary as qs

def tambah_barang(daftar_barang):
    print("\n=== Tambah Barang ===")
    nama = qs.text("Nama barang:").ask()
    harga = qs.text("Harga barang:").ask()
    stok = qs.text("Stok barang:").ask()

    for barang in daftar_barang:
        if barang['nama'].lower() == nama.lower():
            print("Barang sudah ada!")
            return

    konfirmasi = qs.confirm(
        f"Tambahkan '{nama}' (Harga: {harga}, Stok: {stok})?"
    ).ask()
    
    if not konfirmasi:
        print("Penambahan dibatalkan.")
        return

    daftar_barang.append({'nama': nama, 'harga': harga, 'stok': stok})
    print("Barang berhasil ditambahkan!")