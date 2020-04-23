def refund (username_refund):
    id_wahana = input("Masukkan ID Wahana: ")
    jumlah = int(input("Jumlah: "))
    tanggal = input("Masukkan tanggal hari ini: ")
    found = False
    i=0 #Untuk tahu row berapa di file_kepemilikan

    for row in file_kepemilikan:
        if row[0] == username_refund and row[1] == id_wahana:
            found=True
            if jumlah <= int(row[2]):
                temp=int(row[2])-jumlah
                if temp==0:
                    j=1
                    while (file_kepemilikan[i+j][0]!='.'):
                        file_kepemilikan[i]=file_kepemilikan[i+j]
                        j+=1
                    file_kepemilikan[i]=['.','.','.','.','.','.','.']
                else:
                    file_kepemilikan[i][2]=temp
                for row_wahana in file_wahana:
                    if id_wahana == row_wahana[0]:
                        price = int(row_wahana[2])
                j=0
                for row_user in file_user:
                    if username_refund == row_user[3]:
                        temp=int(row_user[6])
                        temp+=price*jumlah
                        row_user[6]=str(temp)
                        file_user[j]=row_user
                        break
                    j+=1
                print("Refund berhasil. Saldo anda sekarang " + row_user[6])
                j=0
                for row_refund in file_refund:
                    if(row_refund[0]=="."):
                        file_refund[j][0]=username_refund
                        file_refund[j][1]=tanggal
                        file_refund[j][2]=id_wahana
                        file_refund[j][3]=jumlah
                    break
                    j+=1
            else:
                print("Anda hanya memiliki " + row[2] + " tiket untuk wahana ini.")
            i+=1
            break

    if not found:
        print("Anda tidak memiliki tiket wahana ini.")
