import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def jeda(pesan = "Tekan Enter untuk melanjutkan..."):
    input(pesan)
