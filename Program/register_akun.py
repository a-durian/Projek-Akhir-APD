import questionary as qs
from fungsi import clear_terminal
import sys
import variabel_global as var


# Fungsi Register Yang Mengambilakan Nilai berupa hak user dan username
# Selain itu Keluar dari Program
def register():
    while True:
        pilihan = qs.select("", ["Register", "Login", "Keluar"]).ask()
        match pilihan:

            case "Register":
                username = input("Input Username : ")
                password = qs.password("Input Password : ").ask()
                if password == "" or username == "":
                    clear_terminal()
                    print("Password atau Username Tidak Boleh Kosong")
                    continue
                username_akun = [i["username"] for i in var.akun.values()]
                if username in username_akun:
                    clear_terminal()
                    print("Username Telah Digunakan")
                    continue
                elif not (username in username_akun):

                    banyak_akun = len(var.akun.values()) + 1
                    var.akun[banyak_akun] = {
                        "username": username,
                        "password": password,
                        "hak": "user",
                    }
                    var.keranjang_belanja[username] = {}
                    var.riwayat_transaksi[username] = {}
                    var.history_pesanan[username] = {}
                    print("Akun Berhasil Di Buat")
                    continue

            case "Login":
                username = input("Input Username : ")
                password = input("Input Password : ")
                for id, akun in var.akun.items():
                    if username == akun["username"] and password == akun["password"]:
                        return [akun["username"], akun["hak"]]
                    elif username == akun["username"] and password != akun["password"]:
                        print("Password Salah")
                        register()
                print("Akun Tidak Di Temukan")
                register()

            case "Keluar":
                sys.exit()
