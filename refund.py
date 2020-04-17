def refund (username):
    id_wahana = input("Masukkan ID Wahana: ")
    jumlah = int(input("Jumlah: "))

    found = False
    i=0 #Untuk tahu row berapa di file_kepemilikan

    for row in file_kepemilikan:
        if row[0] == username and row[1] == id_wahana:
            found=True
            if jumlah <= int(row[2]):
                temp=int(row[2])-jumlah
                if temp==0:
                    del file_kepemilikan[i]
                else:
                    li=list(row)
                    li[2]=str(temp)
                    tup=tuple(li)
                    file_kepemilikan[i]=tup
                    print(file_kepemilikan[i])
                for row_wahana in file_wahana:
                    if id_wahana == row_wahana[0]:
                        price = int(row_wahana[2])
                j=0
                for row_user in file_user:
                    if username == row_user[3]:
                        temp=int(row_user[6])
                        temp+=price*jumlah
                        tup=row_user
                        li=list(tup)
                        li[6]=str(temp)
                        tup=tuple(li)
                        file_user[j]=tup
                    j+=1
                print("Refund berhasil. Saldo anda sekarang " + tup[6])
            else:
                print("Anda hanya memiliki " + row[2] + " tiket untuk wahana ini.")
            i+=1
            
    if not found:
        print("Anda tidak memiliki tiket wahana ini.")
