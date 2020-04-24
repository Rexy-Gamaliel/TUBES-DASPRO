
import load
import basics
import login_user

#searching array kepemilikan
def validasi (arrname, uname, idwahana, jumtiket, leng):
    Found = False
    i=1

    while (Found==False) and (i<leng):
        if arrname[i][0]==uname and arrname[i][1]==idwahana:
            if jumtiket <= int(arrname[i][2]):
                
                sisa = int(arrname[i][2])-jumtiket
                Found=True
                    
                if sisa == 0:
                    basics.delete_row (i,arrname,leng)
                else:
                    arrname[i][2]=str(sisa)
            else:
                i=leng
        else:
            i += 1
            
    return(i,Found,arrname)

def guna_tiket (uname, file_kepemilikan, file_pakai):
    
    id_wahana = input("Masukkan ID wahana: ")
    tanggal = input("Masukkan tanggal hari ini: ")
    jum_tiket = int(input("Jumlah tiket yang digunakan: "))

    le = basics.length(file_kepemilikan)

    (i,found,file_kepemilikan) = validasi (file_kepemilikan, uname, id_wahana, jum_tiket, le)

    if (found==False):
        print ("Tiket Anda tidak valid dalam sistem kami")
        
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

guna_tiket(login_user.ceklogin(),file_kepemilikan, file_pakai)
