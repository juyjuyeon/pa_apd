from storage import data_user
from simpan_fungsi import jeda
from prettytable import PrettyTable

username_pengguna = data_user


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


