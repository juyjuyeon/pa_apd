from simpan_fungsi import jeda
from prettytable import PrettyTable


def read_user(user, daftar_review):
    ulasan_saya = [r for r in daftar_review if r.get("username") == user.get("username")]
    if len(ulasan_saya) == 0:
            print("belum ada ulasan yang tersimpan")
    else: 
        tabel = PrettyTable()
        tabel.field_names = ["No", "Judul", "Genre", "Rating", "Ulasan"]
        for i, review in enumerate(daftar_review): 
            tabel.add_row([
                i + 1, 
                review["judul"], 
                review["genre"], 
                review["rating"], 
                review["ulasan"]
            ])
        print(tabel)
    jeda()
    return ulasan_saya
