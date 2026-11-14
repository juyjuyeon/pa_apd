from prettytable import PrettyTable
from create_admin import daftar_film
from simpan_fungsi import jeda
import inquirer

# def update_admin(daftar_film): 
#     if len(daftar_film) == 0:
#         print("daftar film masih kosong")
#         jeda()
#         return daftar_film

#     while True: 
#         pilih_judul = [
#             inquirer.List(
#                 'edit',
#                 message= "ulasan yang ingin anda ubah",
#                 choices= [ulasan["judul"] for ulasan in daftar_film] 
#             )
#         ]
#         answers = inquirer.prompt(pilih_judul)
#         if not answers:
#             return
#         judul_target = answers['edit']
#         break

#     data_target = None
#     for ulasan in daftar_film: 
#         if ulasan["judul"] == judul_target: 
#             data_target = ulasan
#             break 

#     pilih = [
#         inquirer.List(
#             'opsi',
#             message=f"bagian mana dari '{judul_target} yang ingin diubah?",
#             choices=['judul', 'genre', 'semua data', 'batal']
#         )
#     ]

#     answers_pilih = inquirer.prompt(pilih)
#     opsi_terpilih = answers_pilih['opsi']

#     if opsi_terpilih == 'judul':
#         input_baru = [inquirer.Text('nilai', message="Masukkan judul baru")]
#         hasil = inquirer.prompt(input_baru)
#         data_target['rating'] = hasil['nilai']

#     elif opsi_terpilih == 'genre':
#         input_baru = [inquirer.Text('nilai', message="Masukkan genre baru")]
#         hasil = inquirer.prompt(input_baru)
#         data_target['ulasan'] = hasil['nilai']

#     elif opsi_terpilih == 'Semua Data':
#         form_semua = [
#             inquirer.Text('rating', message="Masukkan rating baru", default=data_target['rating']),
#             inquirer.Text('ulasan', message="Masukkan ulasan baru", default=data_target['ulasan'])
#         ]
#         hasil = inquirer.prompt(form_semua)
#         data_target['judul'] = hasil['judul']
#         data_target['genre'] = hasil['genre']
#     elif opsi_terpilih == 'batal':
#         print("Perubahan dibatalkan.")
#         return
#     print("berhasil memperbarui ulasan")
#     return daftar_film 

import inquirer
from simpan_fungsi import jeda


def update_admin(daftar_film):
    if len(daftar_film) == 0:
        print("Daftar film masih kosong.")
        jeda()
        return daftar_film

    answers = [
        inquirer.List(
            'edit',
            message="Pilih film yang ingin Anda ubah:",
            choices=[film["judul"] for film in daftar_film] + ["kembali"]
        )
    ]
    answers = inquirer.prompt(answers)
    if not answers or answers['edit'] == "kembali":
        return daftar_film

    judul_target = answers['edit']
    data_target = next((f for f in daftar_film if f["judul"] == judul_target), None)

    for film in daftar_film:
        if film["judul"] == judul_target:
            data_target = film
            break

    pilih = [
        inquirer.List(
            'opsi',
            message=f"Bagian mana dari '{judul_target}' yang ingin diubah?",
            choices=['Judul', 'Genre', 'Semua Data', 'Batal']
        )
    ]
    answers_pilih = inquirer.prompt(pilih)
    if not answers_pilih or answers_pilih['opsi'] == 'Batal':
        print("Perubahan dibatalkan.")
        jeda()
        return daftar_film

    opsi_terpilih = answers_pilih['opsi']

    if opsi_terpilih == 'Judul':
        hasil = inquirer.prompt([
            inquirer.Text('judul', message="Masukkan judul baru", default=data_target.get('judul', ''))
        ])
        if hasil and hasil['judul'].strip():
            data_target['judul'] = hasil['judul'].strip()
        else:
            print("Judul tidak boleh kosong. Perubahan dibatalkan.")
            jeda()
            return daftar_film

    elif opsi_terpilih == 'Genre':
        hasil = inquirer.prompt([
            inquirer.Text('genre', message="Masukkan genre baru", default=data_target.get('genre', ''))
        ])
        if hasil and hasil['genre'].strip():
            data_target['genre'] = hasil['genre'].strip()
        else:
            print("Genre tidak boleh kosong. Perubahan dibatalkan.")
            jeda()
            return daftar_film

    elif opsi_terpilih == 'Semua Data':
        form_semua = [
            inquirer.Text('judul', message="Masukkan judul baru", default=data_target.get('judul', '')),
            inquirer.Text('genre', message="Masukkan genre baru", default=data_target.get('genre', ''))
        ]
        hasil = inquirer.prompt(form_semua)
        if hasil and hasil['judul'].strip() and hasil['genre'].strip():
            data_target['judul'] = hasil['judul'].strip()
            data_target['genre'] = hasil['genre'].strip()
        else:
            print("Judul dan genre tidak boleh kosong. Perubahan dibatalkan.")
            jeda()
            return daftar_film

    print("Berhasil memperbarui data film!")
    jeda()
    return daftar_film