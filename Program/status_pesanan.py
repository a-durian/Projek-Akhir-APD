from prettytable import PrettyTable
from datetime import datetime, timedelta
from copy import deepcopy
from fungsi import clear_terminal
import pandas as pd
import variabel_global as var


def status(username):
    if var.riwayat_transaksi[username]:
        # Tampilkan Status Pesanan
        print("Berikut Daftar Status Pesanan Mu")
        salinan_riwayat = deepcopy(var.riwayat_transaksi)
        for no, i in enumerate(var.riwayat_transaksi[username].values(), start=1):
            tabel_status = PrettyTable()
            total = 0
            tabel_status.field_names = ["No", "Nama Produk", "Harga", "Jumlah"]
            for id, barang in enumerate(i["barang"].values(), start=1):
                tabel_status.add_row(
                    [id, barang["nama"], barang["harga"], barang["jumlah"]]
                )
                total += barang["jumlah"] * barang["harga"]
            tabel_status.add_row(["", "", "", ""])
            tabel_status.add_row(["", "", "Total", total])
            print(tabel_status)

            # cek pengiriman sudah sampai atau belum
            if i["waktu_estimasi"] <= datetime.now():
                # barang sudah sampai akan  di hapus dari status Pesanan
                print("Barang Pesanan Mu Sudah Sampai \n")
                var.history_pesanan[username][
                    len(var.history_pesanan[username]) + 1
                ] = salinan_riwayat[username].pop(no)

                # menambah data barang yang telah sampai ke data pemasukan
                for id, pesanan in enumerate(
                    var.riwayat_transaksi[username].values(), start=1
                ):
                    for barang in pesanan["barang"].values():
                        data_baru = {
                            "Tanggal": [pesanan["waktu_estimasi"]],
                            "Nama Barang": [barang["nama"]],
                            "Harga": [barang["harga"]],
                            "Jumlah": [barang["jumlah"]],
                        }
                    df_baru = pd.DataFrame(data_baru)
                    df_baru.to_csv(
                        "data_pemasukan.csv", mode="a", header=False, index=False
                    )

            else:
                print("Barang Pesanan Mu Belum Sampai \n")
            var.riwayat_transaksi[username] = deepcopy(salinan_riwayat[username])
    else:
        clear_terminal()
        print("Maaf Belum Ada Daftar Pesanan Mu")
