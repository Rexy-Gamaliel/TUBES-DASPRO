def topup():
    username=input("Masukkan username: ")
    topup=int(input("Masukkan saldo yang di-top up: "))
    found = False
    i=0
    for row in file_user:
        if row[3] == username:
            found = True
            row[6]= str(int(row[6]) + topup)
            file_user[i]=row
            print("Top up berhasil. Saldo " + str(row[0]) + " bertambah menjadi " + str(row[6]))
        i+=1
    if not found:
      print("Pemain tidak ditemukan")

topup()
