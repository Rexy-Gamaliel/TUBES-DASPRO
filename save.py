import csv

def fromArray(arrayname, filename):
    #Fungsi ini me-rewrite, tidak meng-append
    f = open(filename, 'w')
    
    for row in arrayname:
        firstField = True
        for field in row:
            if (field == '.'):
                break
            elif (firstField):
                f.write(field)
                firstField = False
            else:
                f.write(',' + field)
        if (field == '.'):
            break
        f.write('\n')

def save_file(file_user, file_wahana, file_beli, file_pakai, file_kepemilikan, file_refund, file_ks):
#   Parameter save_file() adalah nama-nama array sebagai berikut:
#	arrayname:	            filename:
#	file_user		        user
#	file_wahana		        wahana
#	file_beli	            beli_tiket
#	file_pakai	            guna_tiket
#	file_kepemilikan	    milik_tiket
#	file_refund		        refund
#	file_ks     	        kritiksaran
#        file_hilang             hilang
#   Fungsi fromArray(arrayname, filename) memindahkan data array ke csv


    user = input('Masukkan nama File User: ')
    fromArray(file_user, user)
    
    wahana = input('Masukkan nama File Daftar Wahana: ')
    fromArray(file_wahana, wahana)
    
    beli_tiket = input('Masukkan nama File Pembelian Tiket: ')
    fromArray(file_beli, beli_tiket)
    
    guna_tiket = input('Masukkan nama File Penggunaan Tiket: ')
    fromArray(file_pakai, guna_tiket)
    
    milik_tiket = input('Masukkan nama File Kepemilikan Tiket: ')
    fromArray(file_kepemilikan, milik_tiket)
    
    refund = input('Masukkan nama File Refund Tiket: ')
    fromArray(file_refund, refund)
    
    kritiksaran = input('Masukkan nama File Kritik dan Saran: ')
    fromArray(file_ks, kritiksaran)
    
    hilang = input('Masukkan nama File Kehilangan Tiket: ')
    fromArray(file_hilang, hilang)
    
    print("File perusahaan Willy Wangky's Chocolate Factory telah di-save.")

