import load

#searching user
def login_user (arrname,username,password,leng):  
    found = False
    i=0
    while (found == False) and (i<leng):
        if arrname[i][3]==username :
            if arrname[i][4]==password :
                found = True
            else:
                i=leng
        else:
            i += 1
    return (i,found)

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

    (i,Found) = login_user(arr_user, uname, pas,le)
    
    while (Found == False):
        print ("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
        uname = input("Masukkan username: ")
        pas = input("Masukkan password: ")
        (i,Found) = login_user(arr_user, uname, pas, le)

    print ("Selamat bersenang-senang,",arr_user[i][0],"!")

ceklogin()