
import load
import save
import login_user_

#searching array kepemilikan
def validasi (arrname, uname, idwahana, jumtiket, leng):
    Found = False
    i=0
    while (Found==False) and (i<leng):
        if arrname[i][0]==uname and arrname[i][1]==idwahana:
            if jumtiket <= int(arrname[i][2]):
                
                sisa = int(arrname[i][2])-jumtiket
                print("sisa",sisa)
                Found=True
                    
                if sisa == 0:
                    del arrname[i]
                else:
                    arrname[i][2]==sisa    
            else:
                i=leng
        else:
            i += 1
            
    return(i,Found,arrname)

def guna_tiket (uname):
    
    id_wahana = input("Masukkan ID wahana: ")
    tanggal = input("Masukkan tanggal hari ini: ")
    jum_tiket = int(input("Jumlah tiket yang digunakan: "))

    file_kepemilikan = toArray("kepemilikan_tiket.csv")
    print("file kepemilikan berhasil")
    file_pakai = toArray("penggunaan.csv")
    print("file pakai berhasil")
    
    #hitung len array
    le = 0      
    for row in file_kepemilikan:
        if row[0]=='.':
            break
        else:
            le += 1

    (i,found,file_kepemilikan) = validasi (file_kepemilikan, uname, id_wahana, jum_tiket, le)

    while (found==False):
        print ("Tiket Anda tidak valid dalam sistem kami")
        id_wahana = input("Masukkan ID wahana (masukkan 999 jika ingin membatalkan): ")
        if id_wahana == "999":
            break
        jum_tiket = int(input("Jumlah tiket yang digunakan: "))
        (i,found,file_kepemilikan) = validasi (file_kepemilikan, uname, id_wahana, jum_tiket, le)
    #print("berhasil")

    fromArray(file_kepemilikan,"kepemilikan_tiket.csv")
    print("berhasil1")
    
    j=0
    for row_pakai in file_pakai :
        if(row_pakai[0]=="."):
            file_pakai[j][0]=uname
            file_pakai[j][1]=tanggal
            file_pakai[j][2]=id_wahana
            file_pakai[j][3]=str(jum_tiket)
            break
        j+=1
    fromArray(file_pakai,"penggunaan.csv")
    print("berhasil")

guna_tiket('aron01')
