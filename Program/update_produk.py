import questionary as qs
from lihat_daftar_barang import listProduk
import variabel_global as var


def update_barang():

    if not var.daftar_barang:
        print("\n ! Belum ada barang untuk diupdate !\n")
        return
    listProduk()
    nama = qs.text("Masukkan nama barang yang ingin diupdate:").ask()

    for barang in var.daftar_barang.values():
        if barang["nama"].lower() == nama.lower():
            konfirmasi = qs.confirm(
                f"Yakin ingin mengupdate barang '{barang['nama']}'?"
            ).ask()

            if not konfirmasi:
                print("\n! Update dibatalkan !\n")
                return

            nama_baru = qs.text("Nama baru (kosongkan jika tidak diubah):").ask()
            harga_baru = qs.text("Harga baru (kosongkan jika tidak diubah):").ask()
            stok_baru = qs.text("Stok baru (kosongkan jika tidak diubah):").ask()
            if nama_baru == "" and harga_baru == "" and stok_baru == "":
                print("\n ! Tidak ada perubahan yang dilakukan. !\n")
                return
            try:
                barang["nama"] = nama_baru or barang["nama"]
                barang["harga"] = int(harga_baru) or barang["harga"]
                barang["stock"] = int(stok_baru) or barang["stock"]
                print("\n+ Barang berhasil diperbarui! \n")
                return
            except ValueError:
                print("Input Tidak Valid")
                return

    print("\n ! Barang tidak ditemukan. !\n")
