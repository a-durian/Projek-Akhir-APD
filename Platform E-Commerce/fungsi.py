import os, time


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def Loading():
    loading = ["l", "o", "a", "d", "i", "n", "g"]
    batas = 0
    while batas <= 2:
        for i in loading:
            print(f"{i}", end="", flush=True)
            time.sleep(0.1)
        clear_terminal()
        batas += 1
