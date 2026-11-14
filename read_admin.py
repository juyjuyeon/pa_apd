from prettytable import PrettyTable
from simpan_fungsi import jeda

# def read_admin(daftar_review):
#     if len(daftar_review) == 0: 
#         print("anda tidak memiliki daftar film apapun")
#     else: 
#         if not daftar_review: 
#             print("belum ada film yang tersimpan")
#         else: 
#             tabel = PrettyTable()
#             tabel.field_names = ["No", "Judul", "Genre"]
#             for i, film in enumerate(daftar_review): 
#                 tabel.add_row([
#                     i + 1,
#                     film["judul"], 
#                     film["genre"], 
#                     film["genre"],
#                     film["rating"],
#                     film["ulasan"]
#                 ])
#             print(tabel)
#     jeda()
#     return daftar_review

def read_film_admin(daftar_film):
    if len(daftar_film) == 0: 
        print("anda tidak memiliki daftar film apapun")
    else: 
        if not daftar_film: 
            print("belum ada film yang tersimpan")
        else: 
            tabel = PrettyTable()
            tabel.field_names = ["No", "Judul", "Genre"]
            for i, film in enumerate(daftar_film, start=1):
                tabel.add_row([i, film.get("judul", "-"), film.get("genre", "-")])
            print(tabel)
    jeda()
    return daftar_film

def read_admin(daftar_review): 
    if len(daftar_review) == 0:
        print(" belum ada review yang tersimpan")
    else: 
        tabel = PrettyTable()
        tabel.field_names = ["No", "Penulis", "Judul", "Genre", "Rating", "Ulasan"]
        for i, rev in enumerate(daftar_review, start=1):
            tabel.add_row([
                i,
                rev.get("username", "-"),
                rev.get("judul", "-"),
                rev.get("genre", "-"),
                rev.get("rating", "-"),
                rev.get("ulasan", "-")
            ])
        print(tabel)
    jeda()
    return daftar_review
