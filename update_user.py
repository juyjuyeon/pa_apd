from simpan_fungsi import jeda
from read_user import read_user
from storage import simpan_semua

def update_user(user, daftar_review): 
    ulasan_saya = read_user(user, daftar_review)
    if len(ulasan_saya) == 0:
        jeda()
        return daftar_review

    try:
        nomor = int(input("\nMasukkan nomor ulasan Anda yang ingin diubah (0 untuk batal): "))
        if nomor == 0:
            print("Perubahan dibatalkan.")
            jeda()
            return daftar_review
        if nomor < 1 or nomor > len(ulasan_saya):
            print("Nomor tidak valid.")
            jeda()
            return daftar_review
    except ValueError:
        print("Input harus berupa angka!")
        jeda()
        return daftar_review

    target = ulasan_saya[nomor - 1]
    print(f"\nMengubah ulasan untuk '{target['judul']}' (Tekan Enter jika tidak ingin mengubah)")

    while True:
        rating_baru = input(f"Rating baru 1-10 [{target['rating']}]: ").strip()
        if rating_baru == "":
            break
        try:
            angka = int(rating_baru)
            if 1 <= angka <= 10:
                target["rating"] = angka
                break
            else:
                print("Rating harus angka 1-10.")
        except ValueError:
            print("Rating harus berupa angka!")

    ulasan_baru = input(f"Ulasan baru [{target['ulasan']}]: ").strip()
    if ulasan_baru != "":
        target["ulasan"] = ulasan_baru

    simpan_semua()
    print("Ulasan berhasil diperbarui!")
    jeda()
    return daftar_review

