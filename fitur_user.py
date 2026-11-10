from create_admin import daftar_review
from create_user import user_create_review
from read import read_review 
from update import update_review
from delete import delete_review
from keluar import keluar_program
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
                choices=['create', 'read', 'update', 'delete', 'keluar']
            )
        ]
        answers = inquirer.prompt(questions)
        if not answers:
            break 
        menu = answers['fitur']

        if menu == "create": 
            user_create_review(daftar_review)
        elif menu == "read": 
            read_review(daftar_review)
        elif menu == "update": 
            update_review(daftar_review)
        elif menu == "delete":
            delete_review(daftar_review)
        elif menu == "keluar":
            keluar_program(daftar_review)
