from login import login, data_user, register
from create_admin import admin_create_film, daftar_review, daftar_film
from read_user import read_user
from create_user import user_create_review
from update_user import update_user
from delete_user import delete_user
from read_admin import read_admin, read_film_admin
from update_admin import update_admin
from delete_admin import delete_admin, delete_film_admin
from simpan_fungsi import clear_screen
from fitur_admin import baca_akun, status_pengguna, buat
import inquirer
import os


def total_ulasan(user, daftar_review): 
    review_user = [r for r in daftar_review if r.get("username") == user.get("username")]
    total = len(review_user)
    print(f"Review yang Anda miliki: {total}")
    return total

def menu_admin(user):
    while True:
        clear_screen()
        print("====== Menu Admin ======")
        print(f"Total film terdaftar : {len(daftar_film)}")
        print(f"Total review masuk:", len(daftar_review))

        menu = [
            inquirer.List(
                "menu",
                message="Pilih menu: ",
                choices=["Create", "Read", "Update", "Delete", "Exit"]
            )
        ]
        jawaban = inquirer.prompt(menu)
        if not jawaban:
            break

        menu = jawaban["menu"]

        if menu == "Create":
            admin_create_film(daftar_film)

        elif menu == "Read":
            pilihan = inquirer.prompt([
                inquirer.List(
                    "baca",
                    message = "Lihat data apa?",
                    choices = ["Film", "Review", "Akun", "Kembali"]
                )
            ])
            if pilihan:
                if pilihan["baca"] == "Film": 
                    read_film_admin(daftar_film)
                elif pilihan["baca"] == "Review":
                    read_admin(daftar_review)
                elif pilihan["baca"] == "Akun":
                    baca_akun(data_user)

        elif menu == "Update":
            pilihan = inquirer.prompt([
                inquirer.List(
                    "edit",
                    message = "Edit apa?",
                    choices = ["Film", "Akun", "Kembali"]
                )
            ])
            if pilihan:
                if pilihan["edit"] == "Film":
                    update_admin(daftar_film)
                elif pilihan["edit"] == "Akun":
                    status_pengguna(data_user)

        elif menu == "Delete":
            pilihan = inquirer.prompt([
                inquirer.List(
                    "hapus",
                    message="Hapus data apa?",
                    choices=["Film", "Review", "Kembali"]
                )
            ])
            if pilihan:
                if pilihan["hapus"] == "Film":
                    delete_film_admin(daftar_film)
                elif pilihan["hapus"] == "Review":
                    delete_admin(daftar_review)
        elif menu == "Exit":
            break


def menu_user(user):
    while True:
        clear_screen()
        print("====== Menu User ======")
        total_ulasan(user, daftar_review)
        menu = [
            inquirer.List(
                "menu",
                message="Pilih menu: ",
                choices=["Create", "Read", "Update", "Delete", "Exit"]
            )
        ]
        jawaban = inquirer.prompt(menu)
        if not jawaban:
            break
        menu = jawaban["menu"]

        if menu == "Create":
            user_create_review(user, daftar_film, daftar_review)
        elif menu == "Read":
            read_user(user, daftar_review)
        elif menu == "Update":
            update_user(user, daftar_review)
        elif menu == "Delete":
            delete_user(user, daftar_review)
        elif menu == "Exit":
            break


def menu_utama():
    while True:
        clear_screen()
        print("====== Menu ======")
        menu = [
            inquirer.List(
                "menu",
                message="Pilih menu: ",
                choices=["Registrasi", "Login", "Exit"]
            )
        ]
        jawaban = inquirer.prompt(menu)
        if not jawaban:
            break
        menu = jawaban["menu"]

        if menu == "Registrasi":
            register()
        elif menu == "Login":
            user = login()
            if user:
                if user["role"] == "admin":
                    menu_admin(user)
                else:
                    menu_user(user)
        elif menu == "Exit":
            break


if __name__ == "__main__":
    menu_utama()
