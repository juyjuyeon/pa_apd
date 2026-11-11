from login import login, data_user
from create_user import user_create_review
from create_admin import admin_create_film, daftar_review, daftar_film
from read_user import read_user
from read_admin import read_admin
from update_user import update_user
from update_admin import update_admin
from delete_admin import delete_admin
from delete_user import delete_user
from keluar import keluar_program
from fitur_user import opsi as opsi_user
from fitur_admin import liat_ulasan, baca_akun, status_pengguna, buat
from prettytable import PrettyTable
import inquirer
import os

def menu_buat(): 
    while True: 
        questions = [
            inquirer.List(
                'fitur', 
                message="pilih menu kelola data",
                choices=['create', 'read', 'update', 'delete', 'kembali']
            )
        ]
        answers = inquirer.prompt(questions)
        if not answers:
            break 
        menu = answers['fitur']

        if menu == "create": 
            admin_create_film(daftar_film)
        elif menu == "read": 
            read_admin(daftar_film)
        elif menu == "update": 
            update_admin(daftar_film)
        elif menu == "delete":
            delete_admin(daftar_film)
        elif menu == "kembali":
            break

user_aktif = login()

input("tekan enter untuk melanjutkan....")        
os.system('cls')

if not user_aktif: 
    print("gagal login, program dihentikan")
    exit()

if user_aktif.get('role') == 'user' and user_aktif.get('status') == 'aktif':
    opsi_user()
elif user_aktif.get('role') == 'admin': 
    while True: 
        questions = [
            inquirer.List(
                'fitur admin', 
                message="pilih menu",
                choices=['buat ulasan', 'liat ulasan', 'status pengguna', 'akun pengguna', 'kembali', 'keluar']
            )
        ]
        answers = inquirer.prompt(questions)

        if not answers: 
            break 
        menu = answers['fitur admin']

        target = None
        for data in data_user: 
            if data.get('username') == menu: 
                target = data 
                break 
            

            choose = [
        inquirer.List(
            'pilihan',
            message=f"bagian mana dari '{target} yang anda akses?",
            choices=['create', 'liat ulasan', 'status pengguna', 'akun pengguna', 'kembali', 'keluar']
        )
    ]
        opsi_pilihan = answers['fitur admin']

        if opsi_pilihan == 'buat ulasan': 
            menu_buat()
        elif opsi_pilihan == 'liat ulasan': 
            liat_ulasan(daftar_review)
        elif opsi_pilihan == 'status pengguna': 
            status_pengguna(data_user)
        elif opsi_pilihan == 'akun pengguna':
            baca_akun(data_user)
        elif opsi_pilihan == 'kembali':
            login()
        elif opsi_pilihan == 'keluar': 
            exit()