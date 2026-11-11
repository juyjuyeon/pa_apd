from prettytable import PrettyTable
from create_admin import daftar_film
import inquirer

def update_admin(daftar_film): 
    if not daftar_film:
        print("daftar film masih kosong")
        return daftar_film

    while True: 
        pilih_judul = [
            inquirer.List(
                'edit',
                message= "ulasan yang ingin anda ubah",
                choices= [ulasan["judul"] for ulasan in daftar_film]
            )
        ]
        answers = inquirer.prompt(pilih_judul)
        if not answers:
            return
        judul_target = answers['edit']
        break

    data_target = None
    for ulasan in daftar_film: 
        if ulasan["judul"] == judul_target: 
            data_target = ulasan
            break 

    pilih = [
        inquirer.List(
            'opsi',
            message=f"bagian mana dari '{judul_target} yang ingin diubah?",
            choices=['judul', 'genre', 'semua data', 'batal']
        )
    ]

    answers_pilih = inquirer.prompt(pilih)
    opsi_terpilih = answers_pilih['opsi']

    if opsi_terpilih == 'judul':
        input_baru = [inquirer.Text('nilai', message="Masukkan judul baru")]
        hasil = inquirer.prompt(input_baru)
        data_target['rating'] = hasil['nilai']

    elif opsi_terpilih == 'genre':
        input_baru = [inquirer.Text('nilai', message="Masukkan genre baru")]
        hasil = inquirer.prompt(input_baru)
        data_target['ulasan'] = hasil['nilai']

    elif opsi_terpilih == 'Semua Data':
        form_semua = [
            inquirer.Text('rating', message="Masukkan rating baru", default=data_target['rating']),
            inquirer.Text('ulasan', message="Masukkan ulasan baru", default=data_target['ulasan'])
        ]
        hasil = inquirer.prompt(form_semua)
        data_target['judul'] = hasil['judul']
        data_target['genre'] = hasil['genre']
    elif opsi_terpilih == 'batal':
        print("Perubahan dibatalkan.")
        return
    print("berhasil memperbarui ulasan")
    return daftar_film 