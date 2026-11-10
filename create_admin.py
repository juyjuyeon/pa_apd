daftar_review = []
daftar_film = []

def admin_create_film(daftar_film): 
    judul = input("judul film/series : ")
    genre =  input("genre : ")
    # rating = input("rating 1-10: ")
    # ulasan = input("ulasan : ")
    # return {"judul": judul, "genre": genre, "rating": rating, "ulasan": ulasan}
    film_baru = {"judul" : judul, "genre" : genre}
    daftar_film.append(film_baru)
    print(f"film/series '{judul}' berhasil ditambahkan ke database")
    return daftar_film

def total_review(daftar_review): 
    total = len(daftar_review)
    print("review yang anda miliki adalah ", total)
    return total

# def create_review(daftar_review):
#     review_baru = masukkan_data()
#     daftar_review.append(review_baru)
#     print("ulasan berhasil ditambahkan!")
#     total_review(daftar_review)
#     return daftar_review