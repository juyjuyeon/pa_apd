from login import data_user
from login import login
from create_admin import daftar_review, daftar_film
from create_admin import admin_create_film
from read_admin import read_admin
from update_admin import update_admin
from delete_admin import delete_admin
from simpan_fungsi import jeda
from prettytable import PrettyTable
import inquirer

username_pengguna = data_user

def buat(): 
    while True: 
        questions = [
            inquirer.List(
                'fitur', 
                message="pilih menu",
                choices=['create', 'read', 'update', 'delete', 'kembali']
            )
        ]
        answers = inquirer.prompt(questions)
        if not answers:
            break 
        menu = answers['fitur']

        if menu == "create": 
            admin_create_film(daftar_review)
        elif menu == "read": 
            read_admin(daftar_film)
        elif menu == "update": 
            update_admin(daftar_review)
        elif menu == "delete":
            delete_admin(daftar_review)
        elif menu == "kembali":
            login()


def baca_akun(data_user): 
    if len(data_user) == 0:
        print("data akun masih kosong")
    else: 
        tabel = PrettyTable()
        tabel.field_names = ["No", "username", "role", "status"]
        for i, data in enumerate (data_user, start=1): 
            tabel.add_row([i + 1, data["username"], data["role"], data["status"]])
        print(tabel)
    jeda()
    return data_user

def liat_ulasan(daftar_review): 
    if len(liat_ulasan) == 0: 
        print("tidak ada ulasan yang tersimpan")
        return
    table = PrettyTable()
    table.field_names = ["No", "penulis", "judul", "genre", "rating", "ulasan"]

    for i, A in enumerate(daftar_review, start=1): 
        table.add_row([
            i,
            A.get("penulis", ), 
            A.get("judul"), 
            A.get("genre"), 
            A.get("rating"), 
            A.get("ulasan")
        ])
    print(table)
    return daftar_review

def status_pengguna(data_user): 
    if len(data_user) == 0:
        print("Data akun masih kosong.")
        jeda()
        return data_user

    tabel = PrettyTable()
    tabel.field_names = ["No", "Username", "Role", "Status"]
    for i, data in enumerate(data_user, start=1):
        tabel.add_row([i + 1, data["username"], data["role"], data["status"]])
    print(tabel)

    target = input("Masukkan username yang ingin diubah statusnya: ").strip()
    if not target: 
        print("perubahan dibatalkan")
        jeda()
        return data_user
    
    user_ditemukan = False
    for user in data_user: 
        if user['status'] == target: 
            user_ditemukan = True
            if user["role"] == "admin":
                print("Akun admin tidak dapat diblokir!")
            elif user['status'] == 'aktif': 
                user['status'] = 'blokir'
                print(" status pengguna '{target}' berhasil di blokir")
            else:
                user['status'] = 'aktif'
                print(" status pengguna '{target}' berhasl di aktifkan")
    if not user_ditemukan: 
        print(f"pengguna dengan username '{target}' tidak ditemukan")
    jeda()
    return data_user


