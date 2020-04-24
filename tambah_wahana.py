
import load
import save

def tambah_wahana ():
    file_wahana = load.toArray("wahana.csv")
    print("Masukkan informasi wahana yang ditambahkan:")

    idwahana = input("Masukkan ID Wahana: ")
    nama = input("Masukkan Nama Wahana: ")
    harga = input("Masukkan Harga Tiket: ")
    umur = input("Batasan umur: ")
    tinggi = input("Batasan tinggi badan: ")
    print("\n")
    print("Info wahana telah ditambahkan!")

    j=0
    for row_wahana in file_wahana :
        if(row_wahana[0]=="."):
            file_wahana[j][0]=idwahana
            file_wahana[j][1]=nama
            file_wahana[j][2]=harga
            file_wahana[j][3]=umur
            file_wahana[j][4]=tinggi
            break
        j+=1
    save.fromArray(file_wahana,"wahana.csv")

tambah_wahana()
