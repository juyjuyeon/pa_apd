from create_admin import daftar_review
from simpan_fungsi import jeda
from read_user import read_user


def delete_user(user, daftar_review):
    ulasan_saya = read_user(user, daftar_review)
    if len(ulasan_saya) == 0: 
        jeda()
        return daftar_review
    try: 
        nomor_hapus = int(input("masukkan nomor yang ingin dihapus: "))
        if nomor_hapus == 0: 
            print("penghapusan dibatalkan")
            jeda()
            return daftar_review
        
        if nomor_hapus < 1 or nomor_hapus > len(ulasan_saya): 
            print("nomor tidak valid")
            jeda()
            return daftar_review
        
    except ValueError: 
        print("masukkan angka!")
        jeda()
        return daftar_review
    
    indeks = ulasan_saya[nomor_hapus - 1]
    del daftar_review[indeks]
    print("review berhasil dihapus!")
    jeda()
    return daftar_review
