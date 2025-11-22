import questionary as qs
from variabel_global import akun
from fungsi import clear_terminal

def kelola_user():
    while True:
        pilihan = qs.select(
            "=== KELOLA AKUN USER ===",
            choices=[
                "Tambah Akun",
                "Lihat Akun",
                "Ubah Akun",
                "Hapus Akun",
                "Kembali"
            ]
        ).ask()

        if pilihan == "Tambah Akun":
            tambah_akun()

        elif pilihan == "Lihat Akun":
            lihat_akun()

        elif pilihan == "Ubah Akun":
            ubah_akun()

        elif pilihan == "Hapus Akun":
            hapus_akun()

        elif pilihan == "Kembali":
            return


# ================= TAMBAH =================
def tambah_akun():
    username = qs.text("Username:").ask()
    password = qs.password("Password:").ask()

    if password == "" or username == "":
        clear_terminal()
        print("Password atau Username Tidak Boleh Kosong")
        return
    
    daftar_akun = [i["username"] for i in akun.values()]
    if username in daftar_akun:
        clear_terminal()
        print("Username Sudah Ada")
        return

    elif not (username in daftar_akun):
        hak = qs.select(
            "Hak Akses:",
            choices=["admin", "user"]
        ).ask()

        akun_baru = max(akun.keys()) + 1 if akun else 1
        akun[akun_baru] = {
            "username": username,
            "password": password,
            "hak": hak
        }

        print(f"\nAkun '{username}' berhasil ditambahkan!\n")


# ================= LIHAT =================
def lihat_akun():
    print("\nDAFTAR AKUN")
    if not akun:
        print("Belum ada akun.\n")
        return

    for idAkun, data in akun.items():
        print(f"{idAkun}. {data['username']} | Hak: {data['hak']}")
    print()


# ================= UBAH =================
def ubah_akun():
    if not akun:
        print("\nTidak ada akun.\n")
        return

    pilihan = qs.select(
        "Pilih akun yang ingin diubah:",
        choices=[f"{i}. {a['username']}" for i, a in akun.items()]
    ).ask()

    idAkun = int(pilihan.split(".")[0])

    username_baru = qs.text(
        "Username baru:",
        default=akun[idAkun]["username"]
    ).ask()

    password_baru = qs.password("Password baru:").ask()

    hak_baru = qs.select(
        "Hak akses baru:",
        choices=["admin", "user"],
        default=akun[idAkun]["hak"]
    ).ask()

    akun[idAkun] = {
        "username": username_baru,
        "password": password_baru,
        "hak": hak_baru
    }

    print("\nAkun berhasil diperbarui!")

# ================= HAPUS =================
def hapus_akun():
    if not akun:
        print("\nTidak ada akun.\n")
        return

    pilihan = qs.select(
        "Pilih akun yang ingin dihapus:",
        choices=[f"{i}. {a['username']}" for i, a in akun.items()]
    ).ask()

    idAkun = int(pilihan.split(".")[0])

    if akun[idAkun]["hak"] == "admin":
        print("\nAkun admin utama tidak boleh dihapus!\n")
        return

    konfirmasi = qs.confirm(
        f"Yakin hapus akun '{akun[idAkun]['username']}'?"
    ).ask()

    if konfirmasi:
        del akun[idAkun]
        print("\nAkun berhasil dihapus!\n")
kelola_user()