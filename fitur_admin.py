from login import data_user
from create_admin import daftar_review
from create_admin import admin_create_film
from read import read_review
from update import update_review
from delete import delete_review
from keluar import keluar_program
from prettytable import PrettyTable
import inquirer

username_pengguna = data_user


def create(): 
    while True: 
        questions = [
            inquirer.List(
                'fitur', 
                message="pilih menu",
                choices=['create', 'read', 'update', 'delete', 'keluar']
            )
        ]
        answers = inquirer.prompt(questions)
        if not answers:
            break 
        menu = answers['fitur']

        if menu == "create": 
            admin_create_film(daftar_review)
        elif menu == "read": 
            read_review(daftar_review)
        elif menu == "update": 
            update_review(daftar_review)
        elif menu == "delete":
            delete_review(daftar_review)
        elif menu == "keluar":
            keluar_program(daftar_review)

def baca_akun(data_user): 
    if not data_user:
        print("data akun masih kosong")
    else: 
        tabel = PrettyTable()
        tabel.field_names = ["No", "username", "password", "role", "status"]
        for i, data in enumerate (data_user): 
            tabel.add_row([i + 1, data["username"], data["password"], data["role"], data["status"]])
        print(tabel)
        return data_user

def liat_ulasan(daftar_review): 
    if not liat_ulasan: 
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
    baca_akun(data_user)
    target = input("masukkan username yang ingin diubah statusnya")

    user_ditemukan = False

    for user in data_user: 
        if user['status'] == target: 
            user_ditemukan = True

            if user['status'] == 'aktif': 
                user['status'] == 'blokir'
                print(" status pengguna '{target}' berhasil di blokir")
            else:
                user['status'] = 'aktif'
                print(" status pengguna '{target}' berhasl di aktifkan")
    if not user_ditemukan: 
        print(f"pengguna dengan username '{target}' tidak ditemukan")
        
    return data_user


