def tambah_barang(daftar_barang):
    print("\n=== Tambah Barang ===")
    nama = input("Nama barang: ").strip()
    harga = input("Harga barang: ").strip()
    stok = input("Stok barang: ").strip()

    for barang in daftar_barang:
        if barang['nama'].lower() == nama.lower():
            print("Barang sudah ada!")
            return

    daftar_barang.append({'nama': nama, 'harga': harga, 'stok': stok})
    print("Barang berhasil ditambahkan!")