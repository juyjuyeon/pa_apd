limit_login = 3
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
    print("====== nama program!=======")
    limit_login = 3

    for i in range(limit_login):
        username_input = input("Masukkan username: ")
        password_input = pwinput.pwinput(prompt="Masukkan password: ")

        user_terhubung = None

        for user in data_user: 
            if user["username"] == username_input and user["password"] == password_input:
                user_terhubung = user
                break 
        if user_terhubung:
            print(f"selamat datang, {user_terhubung['username']}")
            role = user_terhubung.get('role')
            status = user_terhubung.get('status')
            print(f"role anda : {role}")
            print(f"status anda : {status}")
            return user_terhubung

        else:
            print("username atau password salah. Silahkan coba lagi")
            sisa_login = batas_login(limit_login, i)
            print("sisa percobaan login anda", sisa_login)
            if sisa_login == 0:
                print("percobaan login habis")
                exit()

# def login():
#     for i in range(limit_login):
#             username_input = input("Masukkan username: ")
#             password_input = input("Masukkan password: ")
#             if username_input == (data_user) and password_input == (data_user):  
#                 print("=== Selamat datang", (username_input),"===")
#                 break
#             else: 
#                 print("Username atau password salah. Silakan coba lagi.")
#                 sisa_login = batas_login(limit_login, i)
#                 print("sisa percobaan login anda", sisa_login)
#                 if sisa_login == 0:
#                     print("=== Percobaan login habis. Silahkan coba lagi nanti ===")
#                     exit()


