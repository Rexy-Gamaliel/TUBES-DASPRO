def cari_pemain(file_user):
    # Mencari Pemain
    # Fungsi hanya dapat dilakukan oleh admin, validasi dilakukan di fungsi Utama
    # file_user = ['Nama','Tanggal_Lahir','Tinggi_Badan','Username','Password','Role','Saldo']

    # Kamus Lokal:
    # username: string
    # found: boolean
    # i: integer

    # Mengambil input username pemain yang ingin dicari
    username = input("Masukkan username user: ")

    # Mencari pemain
    found = False
    i=0
    while not found:
        if file_user[i][3] == username:
            found = True
            print("Nama Pemain: " + file_user[i][0])
            print("Tinggi Pemain: " + file_user[i][2] + " cm")
            print("Tanggal Lahir Pemain: " + file_user[i][1])

    if not found:
        print("Pemain tidak ditemukan")
