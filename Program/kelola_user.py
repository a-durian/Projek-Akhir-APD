import questionary as qs
import variabel_global as var
from fungsi import clear_terminal


def Kelola_user():
    while True:
        pilihan = qs.select(
            "=== KELOLA AKUN USER ===",
            choices=["Tambah Akun", "Lihat Akun", "Ubah Akun", "Hapus Akun", "Kembali"],
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

    daftar_var.akun = [i["username"] for i in var.akun.values()]
    if username in daftar_var.akun:
        clear_terminal()
        print("Username Sudah Ada")
        return

    elif not (username in daftar_var.akun):
        hak = qs.select("Hak Akses:", choices=["admin", "user"]).ask()

        var.akun_baru = max(var.akun.keys()) + 1 if var.akun else 1
        var.akun[var.akun_baru] = {
            "username": username,
            "password": password,
            "hak": hak,
        }

        print(f"\nAkun '{username}' berhasil ditambahkan!\n")


# ================= LIHAT =================
def lihat_akun():
    print("\nDAFTAR AKUN")
    if not var.akun:
        print("Belum ada akun.\n")
        return

    for idAkun, data in var.akun.items():
        print(f"{idAkun}. {data['username']} | Hak: {data['hak']}")
    print()


# ================= UBAH =================
def ubah_akun():
    if not var.akun:
        print("\nTidak ada akun.\n")
        return

    pilihan = qs.select(
        "Pilih akun yang ingin diubah:",
        choices=[f"{i}. {a['username']}" for i, a in var.akun.items()],
    ).ask()

    idAkun = int(pilihan.split(".")[0])

    username_baru = qs.text(
        "Username baru:", default=var.akun[idAkun]["username"]
    ).ask()

    password_baru = qs.password("Password baru:").ask()

    hak_baru = qs.select(
        "Hak akses baru:", choices=["admin", "user"], default=var.akun[idAkun]["hak"]
    ).ask()

    var.akun[idAkun] = {
        "username": username_baru,
        "password": password_baru,
        "hak": hak_baru,
    }

    print("\nAkun berhasil diperbarui!")


# ================= HAPUS =================
def hapus_akun():
    if not var.akun:
        print("\nTidak ada akun.\n")
        return

    pilihan = qs.select(
        "Pilih akun yang ingin dihapus:",
        choices=[f"{i}. {a['username']}" for i, a in var.akun.items()],
    ).ask()

    idAkun = int(pilihan.split(".")[0])

    if var.akun[idAkun]["hak"] == "admin":
        print("\nAkun admin utama tidak boleh dihapus!\n")
        return

    konfirmasi = qs.confirm(f"Yakin hapus akun '{var.akun[idAkun]['username']}'?").ask()

    if konfirmasi:
        del var.akun[idAkun]
        print("\nAkun berhasil dihapus!\n")

