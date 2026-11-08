daftar_review = []
def masukkan_data(): 
    judul = input("judul : ")
    genre =  input("genre : ")
    rating = input("rating 1-10: ")
    ulasan = input("ulasan : ")
    return {"judul": judul, "genre": genre, "rating": rating, "ulasan": ulasan}

def total_review(daftar_review): 
    total = len(daftar_review)
    print("review yang anda miliki adalah ", total)
    return total

def create_review(daftar_review):
    review_baru = masukkan_data()
    daftar_review.append(review_baru)
    print("ulasan berhasil ditambahkan!")
    total_review(daftar_review)
    return daftar_review