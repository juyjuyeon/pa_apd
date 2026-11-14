daftar_review = []
daftar_film = []
from simpan_fungsi import jeda

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
            genre =  input("genre : ")
            if len(genre) == 0: 
                raise ValueError("genre tidak boleh kosong")
            break
        except ValueError as e: 
            print(e)
    film_baru = {"judul" : judul, "genre" : genre}
    daftar_film.append(film_baru)
    print(f"film/series '{judul}' berhasil ditambahkan ke database")
    jeda()
    return daftar_film

def total_review(daftar_review): 
    total = len(daftar_review)
    print("review yang anda miliki adalah ", total)
    return total
