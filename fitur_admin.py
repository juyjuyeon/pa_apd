from login import data_user
from create import daftar_review
from create import create_review
from read import read_review
from update import update_review
from delete import delete_review
from keluar import keluar_program
from prettytable import PrettyTable
import inquirer

daftar_review = []

def crud(daftar_review): 
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
            create_review(daftar_review)
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
        tabel.field_names = ["No", "username", "password", "role"]
        for i, data in enumerate (data_user): 
            tabel.add_row([i + 1, data["username"], data["password"], data["role"]])
        print(tabel)
        return data_user

def liat_ulasan(daftar_review):
    read_review(daftar_review)
    return daftar_review

# def update_status(): 

def update_ulasan(): 
    opsi()
