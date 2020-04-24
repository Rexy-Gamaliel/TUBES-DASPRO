def refund (username_refund, file_user, file_kepemilikan, file_wahana, file_refund):
    # Merefund tiket yang dimiliki Pemain
    # Fungsi hanya dapat dilakukan oleh role pemain, validasi dilakukan di fungsi Utama

    # file_user = ['Nama','Tanggal_Lahir','Tinggi_Badan','Username','Password','Role','Saldo']
    # file_kepemilikan = ['Username', 'ID_Wahana', 'Jumlah_Tiket']
    # file_wahana: ['ID_Wahana', 'Nama_Wahana', 'Harga_Tiket', 'Batasan_Umur', 'Batasan_Tinggi']
    # file_refund: ['Username','Tanggal_Refund','ID_Wahana','Jumlah_Tiket

    # Kamus Lokal
    # username_refund: string
    # i,j: integer
    # id_wahana: string
    # jumlah: integer
    # tanggal: string
    # found, founduser: boolean
    # jmlsisa: integer
    # saldo: integer
    # refundprice: integer

    # Mengambil input ID Wahana, jumlah tiket yang direfund, dan tanggal refund
    id_wahana = input("Masukkan ID Wahana: ")
    jumlah = int(input("Jumlah: "))
    tanggal = input("Masukkan tanggal hari ini: ")

    # Mencari apakah pemain memiliki tiket wahana tersebut
    found = False
    i=0 #Untuk tahu row berapa di file_kepemilikan

    while (not found) and (file_kepemilikan[i][0] != '.') and (i<400):
        if file_kepemilikan[i][0] == username_refund and file_kepemilikan[i][1] == id_wahana:
            found=True

            # Mengecek apakah tiket wahana yang dimiliki cukup untuk direfund sesuai dengan jumlah yang diinginkan
            if jumlah <= int(file_kepemilikan[i][2]):
                jmlsisa=int(file_kepemilikan[i][2])-jumlah

                if jmlsisa==0: # Jika setelah tiket direfund, tiket untuk wahana tersebut habis, maka row akan didelete
                    j=0
                    while (file_kepemilikan[i+j][0]!='.'):
                        file_kepemilikan[i+j]=file_kepemilikan[i+j+1]
                        j+=1
                    file_kepemilikan[i+j]=['.','.','.']
                else:   # Jika tiket tidak habis, maka jumlah tiket diubah dengan jumlah tiket yang sekarang
                    file_kepemilikan[i][2]=str(jmlsisa)

                for row_wahana in file_wahana:    # Mencari harga tiket wahana
                    if id_wahana == row_wahana[0]:
                        refundprice = int(row_wahana[2]) // 2 # Refund = setengah harga tiket

                j=0
                founduser=False
                while not founduser:    # Mencari row user di file user dan mengubah saldo
                    if username_refund == file_user[j][3]:
                        if(file_user[j][7]== "Gold"):   #Karena user Gold membeli tiket dengan setengah harga, maka refund yang diberikan dikurangi lagi
                            refundprice=refundprice//2
                        saldo=int(file_user[j][6])
                        saldo+=refundprice*jumlah
                        file_user[j][6]=str(saldo)
                        founduser = True
                    j+=1

                print("Refund berhasil. Saldo anda sekarang " + file_user[j][6])

                j=0 # Menambahkan data ke file refund
                while file_refund[j][0] != '.' :
                    j+=1
                file_refund[j][0]=username_refund
                file_refund[j][1]=tanggal
                file_refund[j][2]=id_wahana
                file_refund[j][3]=str(jumlah)
            else:   # Jika jumlah yang ingin direfund>jumlah yang dimiliki, maka refund gagal
                print("Anda hanya memiliki " + file_kepemilikan[i][2] + " tiket untuk wahana ini.")
        i+=1

    if not found:   # Jika tiket tidak dimiliki, refund gagal
        print("Anda tidak memiliki tiket wahana ini.")

    # Mengembalikan file_user, file_kepemilikan, file_wahana, dan file_refund versi terbaru
    return (file_user, file_kepemilikan, file_wahana, file_refund)
