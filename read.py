daftar_review = []
from create import create_review
from create import masukkan_data

def total_review(daftar_review): 
    total = len(daftar_review)
    print("review yang anda miliki adalah ", total)
    return total

def read_review(daftar_review): 
    from prettytable import PrettyTable
    if not daftar_review:
        print("Belum ada review yang tersimpan.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Judul","genre", "Rating", "Ulasan"]
        for i, review in enumerate(daftar_review):
            tabel.add_row([i + 1, review["judul"], review["genre"], review["rating"], review["ulasan"]])
        print(tabel) 
    return daftar_review