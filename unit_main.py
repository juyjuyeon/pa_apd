from login import login, data_user
from create import create_review
from read import read_review 
from update import update_review
from delete import delete_review
from keluar import keluar_program
from fitur_user import opsi
from fitur_admin import crud, liat_ulasan, baca_akun, opsi
from prettytable import PrettyTable
import inquirer


for user in data_user: 
    if user.get('role') == 'user': 
        opsi()
for user in data_user:
    if data_user.get('role') == 'admin': 
        while True: 
            questions = [
                inquirer.List(
                    'fitur admin', 
                    message="pilih menu",
                    choices=['create', 'read', 'update', 'delete', 'crud', 'liat ulasan', 'akun pengguna','keluar']
                )
            ]
            answers = inquirer.prompt(questions)
            if not answers:
                break 
            menu = answers['fitur admin']

            target = None
            for data in data_user: 
                if data["data"] == menu: 
                    target = data 
                    break 
                

                choose = [
            inquirer.List(
                'pilihan',
                message=f"bagian mana dari '{target} yang anda akses?",
                choices=['create', 'read', 'update', 'delete', 'crud', 'liat ulasan', 'akun pengguna' 'batal']
            )
        ]

        answers_pilihan = inquirer.prompt(choose)
        opsi_pilihan = answers_pilihan['fitur admin']

        if opsi_pilihan == 'create':
            input_baru = [inquirer.Text('nilai', message="Masukkan ulasan baru")]
            hasil = inquirer.prompt(input_baru)
            target['create'] = hasil['nilai']

        elif opsi_pilihan == 'read':
            input_baru = [inquirer.Text('nilai', message="daftar akun pengguna")]
            hasil = inquirer.prompt(input_baru)
            target['read'] = hasil['nilai']

        elif opsi_pilihan == 'update':
            input_baru = [inquirer.Text('nilai', message="Masukkan ulasan baru")]
            hasil = inquirer.prompt(input_baru)
            target['update'] = hasil['nilai']

        elif opsi_pilihan == 'delete':
            input_baru = [inquirer.Text('nilai', message="Masukkan ulasan baru")]
            hasil = inquirer.prompt(input_baru)
            target['update'] = hasil['nilai']
            
    # elif opsi_pilihan == 'Semua Data':
    #     form_semua = [
    #         inquirer.Text('genre', message="Masukkan genre baru", default=data_target['genre']),
    #         inquirer.Text('rating', message="Masukkan rating baru", default=data_target['rating']),
    #         inquirer.Text('ulasan', message="Masukkan ulasan baru", default=data_target['ulasan'])
    #     ]
        # hasil = inquirer.prompt(form_semua)
        # data_target['genre'] = hasil['genre']
        # data_target['rating'] = hasil['rating']
        # data_target['ulasan'] = hasil['ulasan']
    # elif opsi_terpilih == 'Batal':
    #     print("Perubahan dibatalkan.")
    #     return


