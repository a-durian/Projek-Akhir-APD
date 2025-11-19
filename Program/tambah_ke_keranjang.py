import prettytable as PrettyTable
import questionary as qs


def Tambah_Barang_ke_Keranjang():
    # "import lazily" untuk menghindari circular imports
    from lihat_daftar_barang import listProduk
    from main import daftar_barang, keranjang_belanja
    from checkout import daftar_Keranjang_Belanja

    listProduk()
    print("\nMasukkan [0] untuk kembali ke menu awal\n")
    menu_grosir_input = qs.text("Silahkan pilih nomor produk untuk dimasukkan ke keranjang belanja: ").ask()
    if menu_grosir_input.isdigit():
        menu_grosir = int(menu_grosir_input)
        if menu_grosir == 0:
            print("\nKembali ke menu awal...\n")
            # menuCustomer() #>> Hharusnya disini kembali ke menu customer
            pass
        elif menu_grosir in daftar_barang:
            jumlah_input = input("Masukkan jumlah [1/2/...]: ")
            if jumlah_input == "":
                jumlah = 1
            elif jumlah_input.isdigit() and int(jumlah_input) > 0:
                jumlah = int(jumlah_input)
            else:
                print("\n!! Jumlah tidak valid. Silahkan coba lagi.!!\n")
                Tambah_Barang_ke_Keranjang()
            keranjang_belanja[menu_grosir] = keranjang_belanja.get(menu_grosir, 0) + jumlah
            nama = daftar_barang[menu_grosir]['nama']
            harga = daftar_barang[menu_grosir]['harga']
            print(f"\n+ {nama} x{jumlah} seharga Rp.{harga:,} berhasil ditambahkan ke keranjang belanja.\n")
            # opsiLagi(menuCustomer, "Checkout produk lagi?", Tambah_Barang_ke_Keranjang)
            #^^ disini harusnya ada output nanya ntuk coba lagi...
            pass
        else:
            print("\nProduk tidak ditemukan. Silahkan coba lagi.\n")
            Tambah_Barang_ke_Keranjang()
    else:
        print("\n!! Input harus berupa nomor. Silahkan coba lagi. !!\n")
        Tambah_Barang_ke_Keranjang()

if __name__ == "__main__":
    Tambah_Barang_ke_Keranjang()