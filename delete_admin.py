from create_admin import daftar_review
from simpan_fungsi import jeda


def delete_film_admin(daftar_film): 
    if len(daftar_film) == 0: 
        print("anda tidak memiliki daftar film apapun")
        jeda()
        return daftar_film
    
    print("====== Daftar film ======")
    for i, film in enumerate(daftar_film, start=1): 
        print(f"{i}. {film.get('judul')} - oleh {film.get('username', 'Anonim')} (Rating: {film.get('rating')}/10)")

    try: 
        hapus_film = int(input("masukkan nomor film yang ingin anda hapus (0 untuk batal): "))
        if hapus_film == 0:
            print("Penghapusan dibatalkan.")
        elif 1 <= hapus_film <= len(daftar_review):
            terhapus = daftar_review.pop(hapus_film - 1)
            print(f"Film untuk '{terhapus['judul']}' berhasil dihapus!")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input harus berupa angka!")
    jeda()
    return daftar_film

def delete_admin(daftar_review):
    if len(daftar_review) == 0: 
        print("belum ada ulasan yang bisa dihapus")
        jeda()
        return daftar_review
    
    print("====== Daftar Ulasan ======")

    for i, film in enumerate(daftar_review, start=1): 
        print(f"{i}. {film.get('judul')} - oleh {film.get('username', 'Anonim')} (Rating: {film.get('rating')}/10)")

    try: 
        hapus_ulasan = int(input("masukkan nomor ulasan yang ingin anda hapus (0 untuk batal): "))
        if hapus_ulasan == 0:
            print("Penghapusan dibatalkan.")
        elif hapus_ulasan <= 1 or hapus_ulasan <= len(daftar_review): 
            # terhapus = daftar_review.pop(hapus_ulasan - 1)
            terhapus = hapus_ulasan - 1
            print(f"Ulasan untuk '{terhapus['judul']}' berhasil dihapus!")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input harus berupa angka!")
    jeda()
    return daftar_review
