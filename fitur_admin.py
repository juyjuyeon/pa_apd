from storage import simpan_semua, data_user
from simpan_fungsi import jeda
import inquirer
from prettytable import PrettyTable

username_pengguna = data_user

# def buat(): 
#     while True: 
#         questions = [
#             inquirer.List(
#                 'fitur', 
#                 message="pilih menu",
#                 choices=['create', 'read', 'update', 'delete', 'kembali']
#             )
#         ]
#         answers = inquirer.prompt(questions)
#         if not answers:
#             break 
#         menu = answers['fitur']

#         if menu == "create": 
#             admin_create_film(daftar_film)
#         elif menu == "read": 
#             while True: 
#                 questions = [
#                     inquirer.List(
#                         'read', 
#                         message="Pilih menu",
#                         choices=['review', 'film', 'kembali']
#                     )
#                 ]
#                 answers = inquirer.prompt(questions)
#                 if not answers:
#                     break 
#                 menu = answers['fitur']
#                 if questions == "review": 
#                     read_admin(daftar_review)
#                 elif questions == "film": 
#                     read_film_admin(daftar_film)
#         elif menu == "update": 
#             update_admin(daftar_review)
#         elif menu == "delete":
#             delete_admin(daftar_review)
#         elif menu == "kembali":
#             break


def baca_akun(data_user): 
    if len(data_user) == 0:
        print("data akun masih kosong")
    else: 
        tabel = PrettyTable()
        tabel.field_names = ["No", "username", "role", "status"]
        for i, data in enumerate (data_user, start=1): 
            tabel.add_row([i, data["username"], data["role"], data["status"]])
        print(tabel)
    jeda()
    return data_user

def liat_ulasan(daftar_review): 
    if len(daftar_review) == 0: 
        print("tidak ada ulasan yang tersimpan")
        return
    table = PrettyTable()
    table.field_names = ["No", "penulis", "judul", "genre", "rating", "ulasan"]

    for i, A in enumerate(daftar_review, start=1): 
        table.add_row([
            i,
            A.get("username", "-"),  
            A.get("judul", "-"), 
            A.get("genre", "-"), 
            A.get("rating", "-"), 
            A.get("ulasan", "-")
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
        tabel.add_row([i, data["username"], data["role"], data["status"]])
    print(tabel)

    target = input("Masukkan username yang ingin diubah statusnya: ").strip()
    if not target: 
        print("perubahan dibatalkan")
        jeda()
        return data_user
    
    user_ditemukan = False
    for user in data_user: 
        if user['username'] == target: 
            user_ditemukan = True
            if user["role"] == "admin":
                print("Akun admin tidak dapat diblokir!")
            elif user['status'] == 'aktif': 
                user['status'] = 'blokir'
                print(f"status pengguna '{target}' berhasil di blokir")
            else:
                user['status'] = 'aktif'
                print(f"status pengguna '{target}' berhasl di aktifkan")
    if not user_ditemukan: 
        print(f"pengguna dengan username '{target}' tidak ditemukan")
    jeda()
    return data_user


