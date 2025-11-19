def update_barang(daftar_barang):
    if not daftar_barang:
        print("Belum ada barang untuk diupdate.")
        return

    print("\n=== Daftar Barang ===")
    for i, barang in enumerate(daftar_barang, start=1):
        print(f"{i}. {barang['nama']} | Harga: {barang['harga']} | Stok: {barang['stok']}")

    nama = input("\nMasukkan nama barang yang ingin diupdate: ").strip()

    for barang in daftar_barang:
        if barang['nama'].lower() == nama.lower():
            barang['nama'] = input("Nama baru (kosongkan jika tidak diubah): ") or barang['nama']
            barang['harga'] = input("Harga baru (kosongkan jika tidak diubah): ") or barang['harga']
            barang['stok'] = input("Stok baru (kosongkan jika tidak diubah): ") or barang['stok']
            print("Barang berhasil diperbarui!")
            return

    print("Barang tidak ditemukan.")