from prettytable import PrettyTable, TableStyle
from datetime import datetime, timedelta
from copy import deepcopy
from fungsi import clear_terminal
import pandas as pd
import variabel_global as var
from colorama import init, Fore, Style

init(autoreset=True)


def status(username):
    if var.riwayat_transaksi[username]:
        # Tampilkan Status Pesanan
        print("Berikut Daftar Status Pesanan Mu")
        salinan_riwayat = deepcopy(var.riwayat_transaksi)
        for no, info in var.riwayat_transaksi[username].items():
            tabel_status = PrettyTable()
            total = 0
            tabel_status.set_style(TableStyle.SINGLE_BORDER)
            tabel_status.field_names = ["No", "Nama Produk", "Jumlah", "Harga"]
            for id, barang in enumerate(info["barang"].values(), start=1):
                tabel_status.add_row(
                    [id, barang["nama"], barang["jumlah"], f"Rp.{barang['harga']:,}"]
                )
                total += barang["jumlah"] * barang["harga"]
            tabel_status.add_row(["", "", "", ""])
            tabel_status.add_row(["", "", "Total", f"Rp.{total:,}"])
            print(tabel_status)

            # cek pengiriman sudah sampai atau belum
            if info["waktu_estimasi"] <= datetime.now():
                # barang sudah sampai akan  di hapus dari status Pesanan
                print("Barang Pesanan Mu Sudah Sampai \n")
                # lakukan salinan riwayat yang sudah sampai ke history
                var.history_pesanan[username][
                    len(var.history_pesanan[username]) + 1
                ] = deepcopy(info)
                # hapus riwayat yang sudah sampai (geser entry setelahnya ke posisi sekarang)
                key_akhir = len(salinan_riwayat[username])
                for key in range(no, key_akhir):
                    if key < key_akhir:
                        salinan_riwayat[username][key] = salinan_riwayat[username][
                            key + 1
                        ]
                del salinan_riwayat[username][key_akhir]

                # menambah data barang yang telah sampai ke data pemasukan
                for id, pesanan in enumerate(
                    var.riwayat_transaksi[username].values(), start=1
                ):
                    for barang in pesanan["barang"].values():
                        data_baru = {
                            "Tanggal": [
                                pesanan["waktu_estimasi"].replace(
                                    hour=0, minute=0, second=0
                                )
                            ],
                            "Nama Barang": [barang["nama"]],
                            "Harga": [barang["harga"]],
                            "Jumlah": [barang["jumlah"]],
                        }
                    df_baru = pd.DataFrame(data_baru)
                    df_baru.to_csv(
                        "data_pemasukan.csv", mode="a", header=False, index=False
                    )

            else:
                print(f"Barang Pesanan Mu Belum Sampai, Estimasi : ", end="")
                # gunakan single quotes di dalam f-string untuk menghindari konflik kutip
                print(Fore.YELLOW + f"{info['waktu_estimasi']} \n")
        var.riwayat_transaksi[username] = deepcopy(salinan_riwayat[username])

    else:
        clear_terminal()
        print("Maaf Belum Ada Daftar Pesanan Mu")
