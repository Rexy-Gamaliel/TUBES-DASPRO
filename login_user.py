import load

def login_user (arrname, username, password):
    Found = False
    i=1
    while (Found == False) and (i<len(arrname)):
        if (arrname[i][3]==username):
            Found = True
            if (arrname[i][4]==password):
                Found=True       
        else:
            i=i+1
    return (i)

def ceklogin ():
    uname = input("Masukkan username: ")
    pas = input("Masukkan password: ")

    arr_user = toArray("user.csv")
    pjg = len(arr_user)
    i = login_user(arr_user, uname, pas)

    while (i >= pjg):
        print ("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
        uname = input("Masukkan username: ")
        pas = input("Masukkan password: ")
        i = login_user(arr_user, uname, pas)

    print ("Selamat bersenang-senang,",arr_user[i][0],"!")

ceklogin()
