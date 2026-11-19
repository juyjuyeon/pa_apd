
from storage import simpan_semua

def admin_create_film(daftar_film): 
    while True: 
        try: 
            judul = input("judul film/series : ").strip()
            if len(judul) == 0:
                raise ValueError("judul tidak boleh kosong")

            for film in daftar_film:
                if film["judul"].lower() == judul.lower():
                    raise ValueError("film ini sudah terdaftar")
            break 
        except ValueError as e:
            print(e)

    while True: 
        try: 
            genre =  input("genre : ").strip()
            if len(genre) == 0: 
                raise ValueError("genre tidak boleh kosong")
            break
        except ValueError as e: 
            print(e)
    film_baru = {"judul" : judul, "genre" : genre}
    daftar_film.append(film_baru)
    simpan_semua()
    print(f"film/series '{judul}' berhasil ditambahkan ke database")
    return daftar_film

def total_review(daftar_review, user): 
    total = 0
    for review in daftar_review:
        if review["username"] == user["username"]:
            total += 1
    print("Review yang anda miliki adalah ", total)
    return total