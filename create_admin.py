daftar_review = []
daftar_film = []

def admin_create_film(daftar_film): 
    judul = input("judul film/series : ")
    genre =  input("genre : ")
    film_baru = {"judul" : judul, "genre" : genre}
    daftar_film.append(film_baru)
    print(f"film/series '{judul}' berhasil ditambahkan ke database")
    return daftar_film

def total_review(daftar_review): 
    total = len(daftar_review)
    print("review yang anda miliki adalah ", total)
    return total
