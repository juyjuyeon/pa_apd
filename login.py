limit_login = 3
from simpan_fungsi import jeda
import pwinput

data_user = [
    {
        "username" : "admin_utama", 
        "password" : "admin123", 
        "role" : "admin",
        "status" : "aktif"
    },
    {
        "username" : "user1", 
        "password" : "user123", 
        "role" : "user",
        "status" : "aktif"
    }, 
    {
        "username" : "user2", 
        "password" : "user234", 
        "role" : "user",
        "status" : "aktif"
    }, 
    {
        "username" : "user3", 
        "password" : "user345",
        "role" : "user",
        "status" : "aktif"
    },
    { 
        "username" : "user4", 
        "password" : "user456",
        "role" : "user",
        "status" : "aktif"
    }
]

def batas_login(batas, percobaan):
    sisa_login = batas - (percobaan + 1)
    return sisa_login

def login(): 
    print("====== Login =======")

    for i in range(limit_login):
        username_input = input("Masukkan username: ").strip()
        password_input = pwinput.pwinput(prompt="Masukkan password: ")

        user_terhubung = None

        for user in data_user:
            if user.get("username") == username_input and user.get("password") == password_input:
                user_terhubung = user
                break

        if user_terhubung:
            if user_terhubung.get("status") != "aktif":
                print("Akun Anda sedang dinonaktifkan. Hubungi admin.")
                jeda()
                return None

            print(f"\nSelamat datang, {user_terhubung['username']}!")
            print(f"Role Anda   : {user_terhubung['role']}")
            print(f"Status Anda : {user_terhubung['status']}")
            jeda()
            return user_terhubung
        else:
            print("Username atau password salah. Silakan coba lagi.")
            sisa_login = batas_login(limit_login, i)
            print("Sisa percobaan login Anda:", sisa_login)
            if sisa_login == 0:
                print("Percobaan login habis.")
                jeda()
                return None
            
def register():
    print("===== Register =====")
    

    while True:
            username_input = input("Username: ").strip()
            if len(username_input) == 0:
                print("Username tidak boleh kosong.")
            elif " " in username_input:
                print("Username tidak boleh mengandung spasi.")
            elif len(username_input) < 4: 
                print("username minimal 4 karakter")
            elif any(user['username'] == username_input for user in data_user):
                print("Username sudah digunakan!")
            else: 
                break


    while True:
            password_input = pwinput.pwinput("Password: ")
            if len(password_input) == 0:
                print("Password tidak boleh kosong.")
            elif len(password_input)< 6: 
                print("password minimal 6 karakter")
                continue
            konfirmasi = pwinput.pwinput("Konfirmasi password: ")
            if konfirmasi != password_input:
                print("Konfirmasi password tidak cocok.")
            else: 
                break
    
    data_user.append({
        "username": username_input,
        "password": password_input, 
        "role": "user", 
        "status": "aktif"
        })
    print("Registrasi berhasil, silakan login!")
    jeda()

