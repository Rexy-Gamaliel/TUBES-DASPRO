##CONTOH
import csv
fields = ['']
with open ('name', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow (fields)

File User: user.csv
File Daftar Wahana: wahana.csv
File Pembelian Tiket: pembelian.csv
File Penggunaan Tiket: penggunaan.csv
File Kepemilikan Tiket: tiket.csv
File Refund Tiket: refund.csv
File Kritik dan Saran: kritiksaran.csv

##START
import csv
f=open ('user.csv','w') 

#4. login
input ("Masukkan username: ",username)
input ("Masukkan password: "password)
fields = ['uname', 'pas'] #kolom tabel

procedure (validasi) #validasi selalu looping
Ketemu = False
search kolom uname
    if  (username = uname):
        Ketemu = True
        search kolom pas
            if (password = pas):
                Ketemu = True
            #else: ketemu = False
    else:
        Ketemu=False

if (Ketemu = False):
    print(pesan kesalahan)
    repeat
        input (username)
        input (password)
        procedure {sampai ketemu=true}
    until (Ketemu)

#7. wifal
    4 kolom: username, ID Wahana, tanggal, jumlah yang dibeli
#8. menggunakan tiket

input ("Masukkan ID wahana: ")
input ("Masukkan tanggal hari ini: ") 
input ("Jumlah tiket yang dgunakan: ")

refer ke kepemilikan
