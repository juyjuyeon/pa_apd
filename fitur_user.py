from create_admin import daftar_review
from create_admin import daftar_film
from login import login 
from create_user import user_create_review
from read_user import read_user 
from update_user import update_user
from delete_user import delete_user
# from simpan_fungsi import jeda
from prettytable import PrettyTable
import inquirer

def liat_ulasan(daftar_review): 
    if not daftar_review:
        print("Belum ada review yang tersimpan.")
    else:
        table = PrettyTable()
        table.field_names = ["No", "judul", "genre", "rating", "ulasan"]
        for i, review in enumerate(daftar_review):
            table.add_row([i + 1, review["judul"], review["genre"], review["rating"], review["ulasan"]   ])
        print(table)

def opsi(): 
    while True: 
        questions = [
            inquirer.List(
                'fitur', 
                message="pilih menu",
                choices=['create', 'read', 'update', 'delete', 'kembali', 'keluar']
            )
        ]
        answers = inquirer.prompt(questions)
        if not answers:
            break 
        menu = answers['fitur']

        if menu == "create": 
            user_create_review(daftar_film)
        elif menu == "read": 
            read_user(daftar_review)
        elif menu == "update": 
            update_user(daftar_review)
        elif menu == "delete":
            delete_user(daftar_review)
        elif menu == "kembali":
            login()
        elif menu == "keluar": 
            exit()
