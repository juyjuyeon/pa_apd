from prettytable import PrettyTable
import inquirer
from create_admin import daftar_review

def total_review(daftar_review): 
    total = len(daftar_review)
    print("review yang anda miliki adalah ", total)
    return total

def update_user(daftar_review): 
    if not daftar_review:
        print("daftar ulasan masih kososng")
        return daftar_review

    while True: 
        pilih_judul = [
            inquirer.List(
                'edit',
                message= "ulasan yang ingin anda ubah",
                choices= [review["judul"] for review in daftar_review]
            )
        ]
        answers = inquirer.prompt(pilih_judul)
        if not answers:
            return
        judul_target = answers['edit']
        break

    data_target = None
    for review in daftar_review: 
        if review["judul"] == judul_target: 
            data_target = review
            break 

    pilih = [
        inquirer.List(
            'opsi',
            message=f"bagian mana dari '{judul_target} yang ingin diubah?",
            choices=['rating', 'ulasan', 'semua data', 'batal']
        )
    ]

    answers_pilih = inquirer.prompt(pilih)
    opsi_terpilih = answers_pilih['opsi']

    if opsi_terpilih == 'rating':
        input_baru = [inquirer.Text('nilai', message="Masukkan rating baru")]
        hasil = inquirer.prompt(input_baru)
        data_target['rating'] = hasil['nilai']

    elif opsi_terpilih == 'ulasan':
        input_baru = [inquirer.Text('nilai', message="Masukkan ulasan baru")]
        hasil = inquirer.prompt(input_baru)
        data_target['ulasan'] = hasil['nilai']

    elif opsi_terpilih == 'Semua Data':
        form_semua = [
            inquirer.Text('rating', message="Masukkan rating baru", default=data_target['rating']),
            inquirer.Text('ulasan', message="Masukkan ulasan baru", default=data_target['ulasan'])
        ]
        hasil = inquirer.prompt(form_semua)
        data_target['rating'] = hasil['rating']
        data_target['ulasan'] = hasil['ulasan']
    elif opsi_terpilih == 'batal':
        print("Perubahan dibatalkan.")
        return
    print("berhasil memperbarui ulasan")
    return daftar_review