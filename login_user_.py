import load

#searching user
def login_user (arrname,username,password):  
    found = False
    i=0
    for row in arrname:
        if arrname[i][3]==username :
            found = True
            if arrname[i][4]==password :
                found = True
        else:
            i += 1
    return (i)

def ceklogin ():
    uname = input("Masukkan username: ")
    pas = input("Masukkan password: ")

    arr_user = toArray("user.csv")

    #hitung len array
    le = 0      
    for row in arr_user:
        if row[0]=='.':
            break
        else:
            le += 1

    i = login_user(arr_user, uname, pas)
    
    while (i >= le):
        print ("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
        uname = input("Masukkan username: ")
        pas = input("Masukkan password: ")
        i = login_user(arr_user, uname, pas)

    print ("Selamat bersenang-senang,",arr_user[i][0],"!")

ceklogin()
