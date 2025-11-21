import questionary as qs

def update_barang(daftar_barang):
    if not daftar_barang:
        print("Belum ada barang untuk diupdate.")
        return

    print("\n=== Daftar Barang ===")
    for i, barang in enumerate(daftar_barang, start=1):
        print(f"{i}. {barang['nama']} | Harga: {barang['harga']} | Stok: {barang['stok']}")

    nama = qs.text("Masukkan nama barang yang ingin diupdate:").ask()

    for barang in daftar_barang:
        if barang['nama'].lower() == nama.lower():
            konfirmasi = qs.confirm(
                f"Yakin ingin mengupdate barang '{barang['nama']}'?"
            ).ask()
            
            if not konfirmasi:
                print("Update dibatalkan.")
                return
            
            nama_baru = qs.text("Nama baru (kosongkan jika tidak diubah):").ask()
            harga_baru = qs.text("Harga baru (kosongkan jika tidak diubah):").ask()
            stok_baru = qs.text("Stok baru (kosongkan jika tidak diubah):").ask()
            
            barang['nama'] = nama_baru or barang['nama']
            barang['harga'] = harga_baru or barang['harga']
            barang['stok'] = stok_baru or barang['stok']
            print("Barang berhasil diperbarui!")
            return

    print("Barang tidak ditemukan.")