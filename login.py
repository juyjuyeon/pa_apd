import os 
import pwinput
data_user = [ 
    {
        "username" : "admin_utama", 
        "password" : "admin123", 
        "role" : "admin"
    },
    {
        "username" : "user1", 
        "password" : "user123", 
        "role" : "user"
    }, 
    {
        "username" : "user2", 
        "password" : "user234", 
        "role" : "user"
    }, 
    {
        "username" : "user3", 
        "password" : "user345",
        "role" : "user"
    },
    { 
        "username" : "user4", 
        "password" : "user456",
        "role" : "user"
    }
]


def login(): 
    print("====== nama program!=======")
    limit_login = 3
    for i in range(limit_login):
        username_input = input("Masukkan username: ")
        password_input = pwinput.pwinput(prompt="Masukkan password: ")
        for u in data_user:
            if username_input == u["username"] and password_input == u["password"]:
                print(f"=== Selamat datang {username_input} ===")
                print(f"Anda login sebagai {u['role']}")
                return 
        else:
            print("Username atau password salah. Silakan coba lagi.")
            sisa_login = limit_login - (i + 1)
            print("sisa percobaan login anda", sisa_login)
            if sisa_login == 0:
                print("=== Percobaan login habis. Silahkan coba lagi nanti ===")
                exit()
input("tekan enter untuk melanjutkan....")        
os.system('cls')
login()


