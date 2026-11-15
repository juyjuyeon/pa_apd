import json
import os

FILE_USER = "data_user.json"
FILE_REVIEW = "daftar_review.json"
FILE_FILM = "daftar_film.json"

def simpan_data(nama_file, data):
    with open(nama_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def muat_data(nama_file, default):
    if not os.path.exists(nama_file):
        simpan_data(nama_file, default)
        return default
    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return default

data_user = muat_data(FILE_USER, [
    {
        "username": "admin_utama",
        "password": "admin123",
        "role": "admin",
        "status": "aktif"
    },
    {
        "username": "user1",
        "password": "user123",
        "role": "user",
        "status": "aktif"
    },
    {
        "username": "user2",
        "password": "user234",
        "role": "user",
        "status": "aktif"
    },
    {
        "username": "user3",
        "password": "user345",
        "role": "user",
        "status": "aktif"
    }
])

daftar_review = muat_data(FILE_REVIEW, [])
daftar_film = muat_data(FILE_FILM, [])

def simpan_semua():
    simpan_data(FILE_USER, data_user)
    simpan_data(FILE_REVIEW, daftar_review)
    simpan_data(FILE_FILM, daftar_film)