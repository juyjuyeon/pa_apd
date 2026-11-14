from prettytable import PrettyTable
import inquirer
from simpan_fungsi import jeda
from read_user import read_user
from create_admin import daftar_review

def update_user(user, daftar_review): 
    ulasan_saya = read_user(user, daftar_review)
    if len(ulasan_saya) == 0:
        print("daftar ulasan masih kososng")
        jeda()
        return daftar_review

    try:
        nomor = int(input("\nMasukkan nomor ulasan Anda yang ingin diubah (0 untuk batal): "))
        if nomor == 0:
            print("Perubahan dibatalkan.")
            jeda()
            return daftar_review
        if nomor < 1 or nomor < len(ulasan_saya):
            print("Nomor tidak valid.")
            jeda()
            return daftar_review
    except ValueError:
        print("Input harus berupa angka!")
        jeda()
        return daftar_review

    target = ulasan_saya[nomor - 1]
    print(f"\nMengubah ulasan untuk '{target['judul']}' (Tekan Enter jika tidak ingin mengubah)")

    while True:
        rating_baru = input(f"Rating baru 1-10 [{target['rating']}]: ").strip()
        if rating_baru == "":
            break
        try:
            angka = int(rating_baru)
            if 1 <= angka <= 10:
                target["rating"] = angka
                break
            else:
                print("Rating harus angka 1-10.")
        except ValueError:
            print("Rating harus berupa angka!")

    ulasan_baru = input(f"Ulasan baru [{target['ulasan']}]: ").strip()
    if ulasan_baru != "":
        target["ulasan"] = ulasan_baru

    print("Ulasan berhasil diperbarui!")
    jeda()
    return daftar_review

    #     pilih_judul = [
    #         inquirer.List(
    #             'edit',
    #             message= "ulasan yang ingin anda ubah",
    #             choices= [review["judul"] for review in daftar_review]
    #         )
    #     ]
    #     answers = inquirer.prompt(pilih_judul)
    #     if not answers:
    #         return
    #     judul_target = answers['edit']
    #     break

    # data_target = None
    # for review in daftar_review: 
    #     if review["judul"] == judul_target: 
    #         data_target = review
    #         break 

    # pilih = [
    #     inquirer.List(
    #         'opsi',
    #         message=f"bagian mana dari '{judul_target} yang ingin diubah?",
    #         choices=['rating', 'ulasan', 'semua data', 'batal']
    #     )
    # ]

    # answers_pilih = inquirer.prompt(pilih)
    # opsi_terpilih = answers_pilih['opsi']

    # if opsi_terpilih == 'rating':
    #     input_baru = [inquirer.Text('nilai', message="Masukkan rating baru")]
    #     hasil = inquirer.prompt(input_baru)
    #     data_target['rating'] = hasil['nilai']

    # elif opsi_terpilih == 'ulasan':
    #     input_baru = [inquirer.Text('nilai', message="Masukkan ulasan baru")]
    #     hasil = inquirer.prompt(input_baru)
    #     data_target['ulasan'] = hasil['nilai']

    # elif opsi_terpilih == 'Semua Data':
    #     form_semua = [
    #         inquirer.Text('rating', message="Masukkan rating baru", default=data_target['rating']),
    #         inquirer.Text('ulasan', message="Masukkan ulasan baru", default=data_target['ulasan'])
    #     ]
    #     hasil = inquirer.prompt(form_semua)
    #     data_target['rating'] = hasil['rating']
    #     data_target['ulasan'] = hasil['ulasan']
    # elif opsi_terpilih == 'batal':
    #     print("Perubahan dibatalkan.")
    #     return
    # print("berhasil memperbarui ulasan")
    # return daftar_review