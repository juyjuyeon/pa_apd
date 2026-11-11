from create_admin import daftar_review
from create_admin import daftar_film

def user_create_review(daftar_film, daftar_review):
    if len(daftar_film) == 0: 
        print("belum ada film yang tersedia")
        return daftar_review

    print("daftar film tersedia")
    for i, film in enumerate(daftar_film): 
        print(f"{i + 1}. {film['judul']} (genre : { film['genre']})")

    try: 
        pilihan = int(input("pilih nomor film yang ingin direview"))
        if pilihan < 1 or pilihan > len(daftar_film): 
            print("nomor film tidak valid")
            return daftar_review

        film_terpilih = daftar_film[ pilihan - 1]

    except ValueError: 
        print("masukkan input berupa angka")
        return daftar_review

    print(f"menulis ulasan untuk {film_terpilih['judul']}")
    rating = input("rating 1-10: ")
    ulasan = input("ulasan: ")

    review_baru = { 
        "judul" : film_terpilih["judul"], 
        "genre" : film_terpilih["genre"], 
        "rating" : rating, 
        "ulasan" : ulasan
    }

    daftar_review.append(review_baru)
    return daftar_review

