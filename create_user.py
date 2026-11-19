from storage import simpan_semua
from simpan_fungsi import jeda

def user_create_review(user, daftar_film, daftar_review):
    if len(daftar_film) == 0: 
        print("belum ada film yang tersedia")
        jeda()
        return daftar_review

    print("daftar film tersedia")
    for i, film in enumerate(daftar_film): 
        print(f"{i + 1}. {film['judul']} (genre : { film['genre']})")

    try: 
        pilihan = int(input("pilih nomor film yang ingin direview (0 untuk batal): "))
        if pilihan == 0:
            print("Pembuatan ulasan dibatalkan.")
            jeda()
            return daftar_review
        if pilihan < 1 or pilihan > len(daftar_film): 
            print("nomor film tidak valid")
            jeda()
            return daftar_review

    except ValueError: 
        print("masukkan input berupa angka")
        jeda()
        return daftar_review
    
    film_terpilih = daftar_film[pilihan - 1]
    username_aktif = user.get("username", " ")
    judul_film = film_terpilih.get("judul", " ")
    for review in daftar_review:
        if (
            review.get("username", "").lower() == username_aktif.lower()
            and review.get("judul", "").lower() == judul_film.lower()
        ):
            print("Kamu sudah pernah mereview film ini")
            jeda()
            return daftar_review
        
    print(f"menulis ulasan untuk {film_terpilih['judul']}")

    while True: 
        try: 
            rating = int(input("rating 1-10: "))
            if rating < 1 or rating > 10: 
                raise ValueError
            break
        except ValueError: 
            print("rating harus angka 1-10")

    while True: 
            try: 
                ulasan = input("ulasan: ").strip()
                if len(ulasan) == 0: 
                    raise ValueError("ulasan tidak boleh kosong")
                break
            except ValueError as e: 
                print(e)

    daftar_review.append({
        "username": user["username"],
        "judul": film_terpilih["judul"],
        "genre": film_terpilih["genre"],
        "rating": rating,
        "ulasan": ulasan,
    })
    simpan_semua()
    
    print(f"review untuk '{film_terpilih['judul']}' berhasil disimpan")
    jeda()
    return daftar_review

