from create import daftar_review
from read import read_review
def total_review(daftar_review): 
    total = len(daftar_review)
    print("review yang anda miliki adalah ", total)
    return total

def delete_review(daftar_review):
    if len(daftar_review) == 0: 
        print("tidak ada yang bisa dihapus")
    else: 
        read_review(daftar_review)
        nomor_hapus = int(input("masukkan nomor yang ingin dihapus: "))
        if 1 <= nomor_hapus <= len(daftar_review): 
            try: 
                nomor_hapus
            except ValueError: 
                print("masukkan angka!")
            indeks = nomor_hapus - 1
            del daftar_review[indeks]
            print("review berhasil dihapus!")
    return daftar_review
