import basics

def hilang (file_hilang, file_kepemilikan):
    #Memasukkan data kehilangan tiket
    uname = input("Masukkan username: ")
    tanggal = input ("Tanggal kehilangan tiket: ")
    id_wahana = input ("ID wahana: ")
    jum_tiket = int(input("Jumlah tiket yang dihilangkan: "))

    #Menghitung panjang array
    le = basics.length(file_kepemilikan)

    #Mencari row dalam file_kepemilikan yang sesuai
    i=1
    for row_milik in file_kepemilikan:
        if file_kepemilikan[i][0]==uname and file_kepemilikan[i][1]==id_wahana:

            sisa=int(file_kepemilikan[i][2])-jum_tiket
            file_kepemilikan[i][2]=str(sisa)
            print(file_kepemilikan[i][2])
            break

        else:
            i += 1

    #Memindahkan data kehilangan ke dalam array file_hilang
    j=0
    for row_hilang in file_hilang :
        if(row_hilang[0]=="."):
            file_hilang[j][0]=uname
            file_hilang[j][1]=tanggal
            file_hilang[j][2]=id_wahana
            file_hilang[j][3]=str(jum_tiket)
            break
        j+=1

    #Mengembalikan array file_hilang dan file_kepemilikan
    return (file_hilang, file_kepemilikan)
