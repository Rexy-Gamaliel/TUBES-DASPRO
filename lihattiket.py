def tiket_pemain(file_kepemilikan, file_wahana):
    # Admin bisa melihat jumlah tiket yang dimiliki pemain
    # Fungsi hanya bisa diakses oleh admin, validasi dilakukan di fungsi Utama

    # file_kepemilikan = ['Username', 'ID_Wahana', 'Jumlah_Tiket']
    # file_wahana: ['ID_Wahana', 'Nama_Wahana', 'Harga_Tiket', 'Batasan_Umur', 'Batasan_Tinggi']

    # Mengambil input username
    username = input("Masukkan username: ")

    founduser = False
    printriwayat = False
    for row in file_kepemilikan:    # Mencari apakah pemain memiliki tiket bermain
        if (row[0]==username):
            founduser = True
            foundwahana = False
            i=0
            while not foundwahana:  # Mencari nama wahana di file wahana
                if (file_wahana[i][0] == row[1]):
                    foundwahana=True
                    namawahana=file_wahana[i][1]
                i+=1
            if not printriwayat:    # Mengecek apakah 'Riwayat: ' sudah pernah diprint sebelumnya
                print("Riwayat: ")
                printriwayat = True

            print ("{} | {} | {}".format(row[1],namawahana,row[2]))

    # Case jika pemain tidak memiliki tiket bermain satu pun
    if not founduser:
        print("Pemain tidak memiliki tiket bermain.")
