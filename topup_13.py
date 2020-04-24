def topup(file_user):
    # Melakukan topup saldo username
    # Fungsi hanya dapat dijalankan oleh Admin, validasi dilakukan di menu utama
    # file_user = ['Nama','Tanggal_Lahir','Tinggi_Badan','Username','Password','Role','Saldo','Jenis_Pemain']

    # Kamus Lokal:
    # username: string
    # topup: integer
    # found: boolean
    # i: integer

    # Mengambil input username dan saldo yang ingin di topup
    username=input("Masukkan username: ")
    topup=int(input("Masukkan saldo yang di-top up: "))

    # Mencari Pemain dan mengubah saldo
    found = False
    i=0

    while not found:
        if file_user[i][3] == username:
            found = True
            file_user[i][6]= str(int(file_user[i][6]) + topup)
            print("Top up berhasil. Saldo " + str(file_user[i][0]) + " bertambah menjadi " + str(file_user[i][6]))
        i+=1

    # Jika user tidak ditemukan
    if not found:
      print("Pemain tidak ditemukan")

    # Mengembalikan file_user dengan saldo yang sudah di topup
    return file_user
