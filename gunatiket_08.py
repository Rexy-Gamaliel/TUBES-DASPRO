
import basics
import login_user

#searching array kepemilikan
def validasi (arrname, uname, idwahana, jumtiket, leng):
    #Fungsi melakukan validasi terhadap input user
    Found = False
    i=1

    while (Found==False) and (i<leng):
        if arrname[i][0]==uname and arrname[i][1]==idwahana:
            if jumtiket <= int(arrname[i][2]):
                #Menghitung sisa tiket yang dimiliki user setelah digunakan
                sisa = int(arrname[i][2])-jumtiket
                Found=True

                if sisa == 0:
                    #Menghapus baris array yang memiliki jumlah tiket nol
                    basics.delete_row (i,arrname,leng)
                else:
                    arrname[i][2]=str(sisa)
            else:
                i=leng
        else:
            i += 1

    return(i,Found,arrname)

def guna_tiket (uname, file_kepemilikan, file_pakai):
    #Fungsi meminta input user terkait jumlah tiket yang akan digunakan
    id_wahana = input("Masukkan ID wahana: ")
    tanggal = input("Masukkan tanggal hari ini: ")
    jum_tiket = int(input("Jumlah tiket yang digunakan: "))

    #Menghitung panjang array
    le = basics.length(file_kepemilikan)
    #Melakukan validasi terhadap input user
    (i,found,file_kepemilikan) = validasi (file_kepemilikan, uname, id_wahana, jum_tiket, le)

    #Mencetak pesan kesalahan apabila input tidak valid
    if (found==False):
        print ("Tiket Anda tidak valid dalam sistem kami")

    #Memasukkan data penggunaan tiket user yang valid ke array file_pakai
    #File_pakai adalah array untuk "penggunaan.csv"
    j=0
    for row_pakai in file_pakai :
        if(row_pakai[0]=="."):
            file_pakai[j][0]=uname
            file_pakai[j][1]=tanggal
            file_pakai[j][2]=id_wahana
            file_pakai[j][3]=str(jum_tiket)
            break
        j+=1

    return (file_kepemilikan, file_pakai)
