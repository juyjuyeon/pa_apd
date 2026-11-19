import re
import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def jeda(pesan = "Tekan Enter untuk melanjutkan..."):
    input(pesan)

def validasi_input(pesan, pola):
    while True:
        teks = input(pesan).strip()
        if teks and re.fullmatch(pola, teks):
            return teks
        print("Input tidak valid!")