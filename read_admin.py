from prettytable import PrettyTable

def read_admin(daftar_film):
    if len(daftar_film) == 0: 
        print("anda tidak memiliki daftar film apapun")
    else: 
        if not daftar_film: 
            print("belum ada film yang tersimpan")
        else: 
            tabel = PrettyTable()
            tabel.field_names = ["No", "Judul", "Genre"]
            for i, film in enumerate(daftar_film): 
                tabel.add_row([
                    i + 1,
                    film["judul"], 
                    film["genre"], 
                ])
            print(tabel)
    return daftar_film
