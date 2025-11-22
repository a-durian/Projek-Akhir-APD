import questionary as qs
from lihat_daftar_barang import listProduk
import variabel_global as var


def update_barang():
    if not var.daftar_barang:
        print("Belum ada barang untuk diupdate.")
        return

    print("\n=== Daftar Barang ===")
    listProduk()
    nama = qs.text("Masukkan nama barang yang ingin diupdate:").ask()

    for barang in var.daftar_barang.values():
        if barang["nama"].lower() == nama.lower():
            konfirmasi = qs.confirm(
                f"Yakin ingin mengupdate barang '{barang['nama']}'?"
            ).ask()

            if not konfirmasi:
                print("Update dibatalkan.")
                return

            nama_baru = qs.text("Nama baru (kosongkan jika tidak diubah):").ask()
            harga_baru = qs.text("Harga baru (kosongkan jika tidak diubah):").ask()
            stok_baru = qs.text("Stok baru (kosongkan jika tidak diubah):").ask()

            barang["nama"] = nama_baru or barang["nama"]
            barang["harga"] = int(harga_baru) or barang["harga"]
            barang["stock"] = int(stok_baru) or barang["stock"]
            print("Barang berhasil diperbarui!")
            return

    print("Barang tidak ditemukan.")
