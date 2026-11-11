from create_admin import daftar_film

# def total_review(daftar_review): 
#     total = len(daftar_review)
#     print("review yang anda miliki adalah ", total)
#     return total

def delete_admin(daftar_film): 
    if len(daftar_film) == 0: 
        print("anda tidak memiliki daftar film apapun")
    else: 
        for i, film in enumerate: 
            print(f"{i + 1}. {film['judul']} (genre : { film['genre']})")
        hapus_film = int(input("masukkan nomor film yang ingin anda hapus"))
        if 1 <= hapus_film <= len(daftar_film): 
                    try: 
                        hapus_film
                    except ValueError: 
                        print("masukkan angka!")
                    indeks = hapus_film - 1
                    del daftar_film[indeks]
                    print("review berhasil dihapus!")
    return daftar_film