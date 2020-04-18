def refund ():
    username=input()
    id_wahana = input("Masukkan ID Wahana: ")
    jumlah = int(input("Jumlah: "))
    tanggal = input("Masukkan tanggal hari ini: ")
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
                    row[2]=str(temp)
                    file_kepemilikan[i]=row
                for row_wahana in file_wahana:
                    if id_wahana == row_wahana[0]:
                        price = int(row_wahana[2])
                        print(price)
                j=0 #Untuk tahu row berapa di file_user
                for row_user in file_user:
                    if username == row_user[3]:
                        temp=int(row_user[6])
                        temp+=price*jumlah
                        row_user[6]=str(temp)
                        file_user[j]=row_user
                        break
                    j+=1
                print("Refund berhasil. Saldo anda sekarang " + row_user[6])
            else:
                print("Anda hanya memiliki " + row[2] + " tiket untuk wahana ini.")
            break
            i+=1

        li = [username, tanggal, id_wahana, jumlah]
        file_refund.append(li)
        
    if not found:
        print("Anda tidak memiliki tiket wahana ini.")
