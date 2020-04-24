def upgradeakun(file_user):
    # file_user = ['Nama','Tanggal_Lahir','Tinggi_Badan','Username','Password','Role','Saldo','Jenis_Pemain']

    # Kamus Lokal
    # username: string
    # upgradeprice: integer
    # found: boolean
    # i: integer
    # saldoakhir: integer

    # Mengambil input username yang ingin diupgrade
    username = input("Masukkan username yang ingin di-upgrade: ")
    upgradeprice = 100000

    # Mencari username pemain yang ingin diupgrade
    found=False
    i=0
    while not found:
        if(file_user[i][3]==username):
            found=True
            if(file_user[i][7]=="Gold"):    # Case pemain sudah member gold
                print("Pemain sudah di-upgrade sebelumnya.")
            elif(file_user[i][5]=="Admin"): #Case username yang dimasukkan username admin
                print("User tersebut adalah admin.")
            elif(int(file_user[i][6])<upgradeprice):    # Case pemain tidak memiliki saldo cukup
                print("Pemain tidak memiliki saldo yang cukup untuk upgrade.")
            else:   # Case pemain memenuhi syarat
                saldoakhir= int(file_user[i][6])-upgradeprice
                file_user[i][6]=str(saldoakhir)
                file_user[i][7]="Gold"
                print("Akun {} telah diupgrade.".format(file_user[i][0]))
        i+=1
    return file_user
