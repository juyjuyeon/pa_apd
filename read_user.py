from prettytable import PrettyTable
from simpan_fungsi import jeda

def read_user(user, daftar_review):
    ulasan_saya = [r for r in daftar_review if r.get("username") == user.get("username")]
    
    if not ulasan_saya:
        print("Belum ada ulasan yang tersimpan.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Judul", "Genre", "Rating", "Ulasan"]
        
        for i, review in enumerate(ulasan_saya, start=1):
            tabel.add_row([
                i,
                review.get("judul", "-"),
                review.get("genre", "-"),
                review.get("rating", "-"),
                review.get("ulasan", "-")
            ])
        print(tabel)
    jeda()
    return ulasan_saya