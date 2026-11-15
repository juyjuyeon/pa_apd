from storage import simpan_semua, daftar_review
from simpan_fungsi import jeda
import inquirer

def sinkron_review(judul_lama, data_film):
    for review in daftar_review: 
        if review["judul"] == judul_lama:
            review["judul"] = data_film["judul"]
            review["genre"] = data_film["genre"]

def update_admin(daftar_film):
    if len(daftar_film) == 0:
        print("Daftar film masih kosong.")
        jeda()
        return daftar_film
    
    answers = [
        inquirer.List(
            'edit',
            message="Pilih film yang ingin Anda ubah:",
            choices=[film["judul"] for film in daftar_film] + ["kembali"]
        )
    ]
    answers = inquirer.prompt(answers)
    if not answers or answers['edit'] == "kembali":
        return daftar_film

    judul_target = answers['edit']
    data_target = next((f for f in daftar_film if f["judul"] == judul_target), None)

    for film in daftar_film:
        if film["judul"] == judul_target:
            data_target = film
            break

    pilih = [
        inquirer.List(
            'opsi',
            message=f"Bagian mana dari '{judul_target}' yang ingin diubah?",
            choices=['Judul', 'Genre', 'Semua Data', 'Batal']
        )
    ]
    answers_pilih = inquirer.prompt(pilih)
    if not answers_pilih or answers_pilih['opsi'] == 'Batal':
        print("Perubahan dibatalkan.")
        jeda()
        return daftar_film

    opsi_terpilih = answers_pilih['opsi']

    if opsi_terpilih == 'Judul':
        hasil = inquirer.prompt([
            inquirer.Text('judul', message="Masukkan judul baru", default=data_target.get('judul', ''))
        ])
        if not hasil or not hasil['judul'].strip():
            print("Judul tidak boleh kosong. Perubahan dibatalkan.")
            jeda()
            return daftar_film
        
        judul_baru = hasil['judul'].strip()
        if any(f is not data_target and f["judul"].lower() == judul_baru.lower() for f in daftar_film):
            print("Judul ini sudah terdaftar. Perubahan dibatalkan.")
            jeda()
            return daftar_film

        data_target['judul'] = judul_baru
        sinkron_review(judul_target, data_target)
        simpan_semua()

    elif opsi_terpilih == 'Genre':
        hasil = inquirer.prompt([
            inquirer.Text('genre', message="Masukkan genre baru", default=data_target.get('genre', ''))
        ])
        if hasil and hasil['genre'].strip():
            data_target['genre'] = hasil['genre'].strip()
            sinkron_review(judul_target, data_target)
            simpan_semua()
        else:
            print("Genre tidak boleh kosong. Perubahan dibatalkan.")
            jeda()
            return daftar_film

    elif opsi_terpilih == 'Semua Data':
        form_semua = [
            inquirer.Text('judul', message="Masukkan judul baru", default=data_target.get('judul', '')),
            inquirer.Text('genre', message="Masukkan genre baru", default=data_target.get('genre', ''))
        ]
        hasil = inquirer.prompt(form_semua)

        if not hasil or not hasil['judul'].strip() or not hasil['genre'].strip():
            print("Judul dan genre tidak boleh kosong. Perubahan dibatalkan.")
            jeda()
            return daftar_film

        judul_baru = hasil['judul'].strip()
        if any(f is not data_target and f["judul"].lower() == judul_baru.lower() for f in daftar_film):
            print("Judul ini sudah terdaftar. Perubahan dibatalkan.")
            jeda()
            return daftar_film

        data_target['judul'] = judul_baru
        data_target['genre'] = hasil['genre'].strip()
        sinkron_review(judul_target, data_target)
        simpan_semua()

    print("Berhasil memperbarui data film!")
    jeda()
    return daftar_film