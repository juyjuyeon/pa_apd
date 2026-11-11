
from prettytable import PrettyTable

def total_review(daftar_review): 
    total = len(daftar_review)
    print("review yang anda miliki adalah ", total)
    return total

def read_user(daftar_review):
    if len(daftar_review) == 0: 
        print("belum ada ulasan")
    else: 
        if not daftar_review: 
            print("belum ada review yang tersimpan")
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
    return daftar_review
