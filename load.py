import csv

def toArray (filename):
	f = open('user.csv', 'r')
	file=csv.reader(f)
	row=next(file)

	pjgkolom=0

	for field in row:
	    pjgkolom+=1

	arr = [['string' for j in range (pjgkolom)] for i in range (200)]

	baris=0
	for row in file:
	    kolom=0
	    for field in row:
	        arr[baris][kolom]=field
	        kolom+=1
	    baris+=1

	f.close()

	return(arr)

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

# Ini nanti di fungsi utama ada ini
# (file_user, file_wahana, file_beli, file_pakai, file_kepemilikan, file_refund, file_ks) = load_file()
