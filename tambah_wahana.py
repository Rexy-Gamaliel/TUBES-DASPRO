import load

def tambah_wahana ():
    li = []

    print("Masukkan informasi wahana yang ditambahkan:")

    idwahana = input("Masukkan ID Wahana: ")
    nama = input("Masukkan Nama Wahana: ")
    harga = int(input("Masukkan Harga Tiket: "))
    umur = input("Batasan umur: ")
    tinggi = input("Batasan tinggi badan: ")

    print("Info wahana telah ditambahkan!")

    li = [idwahana, nama, harga, umur, tinggi]
    file_wahana.append(li)
    
tambah_wahana()
