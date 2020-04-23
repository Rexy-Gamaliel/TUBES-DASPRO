import csv

# Nama fisik file .csv, nama logik csv, dan array-nya adalah sebagai berikut:
# csvName:                    fileName:         arrayName:
# user.csv                    user              file_user
# wahana.csv                  wahana            file_wahana
# pembelian.csv               beli_tiket        file_beli
# penggunaan.csv              guna_tiket        file_pakai
# kepemilikan_tiket.csv       milik_tiket       file_kepemilikan
# refund_tiket.csv            refund            file_refund
# kritik_dan_saran.csv        kritiksaran       file_ks


def toArray (filename):
    # Memindahkan data dari csv ke array

    # Pembacaan data
    f = open(filename, 'r')
    file = csv.reader(f)
    row = next(file)
    # Menentukan banyak kolom
    pjgkolom = 0
    for field in row:
	    pjgkolom+=1

    # Deklarasi array berdasarkan data csv
    # row_size menunjukkan berapa NMax maksimum untuk setiap csv
    # Secara berurutan:
    # 0. username(200),
    # 1. wahana(60),
    # 2. pembelian(75),
    # 3. penggunaan(75),
    # 4. kepemilikan(400),
    # 5. refund(75),
    # 6. kritiksaran(100)
    row_size = [200, 60, 75, 75, 400, 75, 100]

    if (filename == 'user.csv'):
        arr = [['.' for j in range (pjgkolom)] for i in range(row_size[0])]
    elif (filename == 'wahana.csv'):
        arr = [['.' for j in range (pjgkolom)] for i in range(row_size[1])]
    elif (filename == 'pembelian.csv'):
        arr = [['.' for j in range (pjgkolom)] for i in range(row_size[2])]
    elif (filename == 'penggunaan.csv'):
        arr = [['.' for j in range (pjgkolom)] for i in range(row_size[3])]
    elif (filename == 'kepemilikan_tiket.csv'):
        arr = [['.' for j in range (pjgkolom)] for i in range(row_size[4])]
    elif (filename == 'refund_tiket.csv'):
        arr = [['.' for j in range (pjgkolom)] for i in range(row_size[5])]
    elif (filename == 'kritik_dan_saran.csv'):
        arr = [['.' for j in range (pjgkolom)] for i in range(row_size[6])]
    else:   #Jaga-jaga kalau nama file .csv tidak mengikuti format
        arr = [['.' for j in range (pjgkolom)] for i in range(200)]

    # Memasukkan data csv ke array
    baris=0
    kolom=0

    # Memasukkan header
    for field in row:
	    arr[baris][kolom]=field
	    kolom+=1
    baris+=1
    # Memasukkan data
    for row in file:
	    kolom=0
	    for field in row:
	        arr[baris][kolom]=field
	        kolom+=1
	    baris+=1

    f.close()
    return(arr)

# Membaca nama file
def load_file():
		user = input('Masukkan nama File User: ')
		file_user = toArray(user)

		wahana = input('Masukkan nama File Daftar Wahana: ')
		file_wahana = toArray(wahana)

		beli_tiket = input('Masukkan nama File Pembelian Tiket: ')
		file_beli = toArray(beli_tiket)

		guna_tiket = input('Masukkan nama File Penggunaan Tiket: ')
		file_pakai = toArray(guna_tiket)

		milik_tiket = input('Masukkan nama File Kepemilikan Tiket: ')
		file_kepemilikan = toArray(milik_tiket)

		refund = input('Masukkan nama File Refund Tiket: ')
		file_refund = toArray(refund)

		kritiksaran = input('Masukkan nama File Kritik dan Saran: ')
		file_ks = toArray(kritiksaran)

		print("File perusahaan Willy Wangky's Chocolate Factory telah di-load.")
		return(file_user, file_wahana, file_beli, file_pakai, file_kepemilikan, file_refund, file_ks)
