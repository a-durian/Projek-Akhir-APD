import questionary as qs
from fungsi import clear_terminal
import sys


# Fungsi Register Yang Mengambilakan Nilai berupa hak user dan username
# Selain itu Keluar dari Program
def register(penyimpanan_akun, keranjang_belanja, riwayat_transaksi, history_pesanan):
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
                username_akun = [i["username"] for i in penyimpanan_akun.values()]
                if username in username_akun:
                    clear_terminal()
                    print("Username Telah Digunakan")
                    continue
                elif not (username in username_akun):

                    banyak_akun = len(penyimpanan_akun.values()) + 1
                    penyimpanan_akun[banyak_akun] = {
                        "username": username,
                        "password": password,
                        "hak": "user",
                    }
                    keranjang_belanja[username] = {}
                    riwayat_transaksi[username] = {}
                    history_pesanan[username] = {}
                    print("Akun Berhasil Di Buat")
                    continue

            case "Login":
                username = input("Input Username : ")
                password = input("Input Password : ")
                for id, akun in penyimpanan_akun.items():
                    for a in akun:
                        if (
                            akun["username"] == username
                            and akun["password"] == password
                        ):
                            if akun["hak"] == "admin":
                                return [akun["username"], akun["hak"]]
                            elif akun["hak"] == "user":
                                return [akun["username"], akun["hak"]]
                            else:
                                return "Keluar"
                        elif (
                            akun["username"] != username or akun["password"] != password
                        ):
                            print("Username atau Password Salah")
                            break
            case "Keluar":
                sys.exit()
