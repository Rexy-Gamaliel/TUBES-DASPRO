# Fungsi Pembelian Tiket
# Pembelian tiket hanya dapat dilakukan oleh pemain yang telah terdaftar dan melakukan login

# Kamus
# ID_wahana, tanggal, nama_wahana, tanggal_lahir: str
# jumlah_tiket, tinggi, saldo, umur, harga_tiket, total_harga : int
# tahun_lahir, tahun_sekarang : int
# syarat_tinggi, syarat_umur, syarat_saldo : bool

# Algoritma
import csv

def toArray (filename):											#kalau udah digabung, fungsi toArraynya boleh dihapus
	f = open(filename, 'r')
	file=csv.reader(f)
	row=next(file)

	pjgkolom=0

	for field in row:
		pjgkolom+=1
		
	arr = [['.' for j in range (pjgkolom)] for i in range (200)]

	baris=0
	kolom=0
	for row in file:
		kolom=0
		for field in row:
			arr[baris][kolom]=field
			kolom+=1
		baris+=1
		
	f.close()
	return(arr)
	
user = input('Masukkan nama File User: ')                          #ini juga bisa dihapus kalau digabung
file_user = toArray(user)
wahana = input('Masukkan nama File Daftar Wahana: ')
file_wahana = toArray(wahana)
beli_tiket = input('Masukkan nama File Pembelian Tiket: ')
file_beli = toArray(beli_tiket)
milik_tiket = input('Masukkan nama File Kepemilikan Tiket: ')
file_kepemilikan = toArray(milik_tiket)                             

def beli(username):												#fungsi utama
	ID_wahana = input('Masukkan ID wahana: ')
	tanggal = input('Masukkan tanggal hari ini: ')
	jumlah_tiket = int(input('Jumlah tiket yang dibeli: '))
	
	syarat_tinggi = False
	syarat_umur = False
	syarat_saldo = False
	
	for row_user in file_user:
		if (row_user[3] == username):
			tinggi = int(row_user[2])
			saldo = int(row_user[6])
			tanggal_lahir = row_user[1]
			tahun_lahir = int(tanggal_lahir[-4:])
			
	tahun_sekarang = int(tanggal[-4:])
	umur = tahun_sekarang - (tahun_lahir)
	
	for row_wahana in file_wahana:
		if (row_wahana[0] == ID_wahana):
			nama_wahana = row_wahana[1]
			harga_tiket = int(row_wahana[2])
			total_harga = harga_tiket*jumlah_tiket
			if (saldo > total_harga):
				syarat_saldo = True
				saldo -= total_harga
			else:
				syarat_saldo = False
			if (row_wahana[4] == '>170') and (row_wahana[3]=='anak-anak'):
				if tinggi >170 and umur>=6 and umur<=12:
					syarat_tinggi = True
					syarat_umur = True
				else:
					syarat_tinggi = False
					syarat_umur = False
			elif (row_wahana[4] == '>170') and (row_wahana[3]=='dewasa'):
				if tinggi >170 and umur>=20 and umur<=45:
					syarat_tinggi = True
					syarat_umur = True
				else:
					syarat_tinggi = False
					syarat_umur = False
			else:
				syarat_tinggi = True
				syarat_umur = True
	
	if (syarat_tinggi==False) or (syarat_umur==False):
		print('Anda tidak memenuhi persyaratan untuk memainkan wahana ini.')
		print('Silakan menggunakan wahana lain yang tersedia.')
	elif (syarat_saldo==False):
		print('Saldo Anda tidak cukup.')
		print('Silakan mengisi saldo Anda.')
	else:
		print('Selamat bersenang-senang di '+ str(nama_wahana))
		pembelian = [username, tanggal, ID_wahana, jumlah_tiket]
		for row_beli in file_beli:
			row_beli[0] = pembelian
			break
		for row_milik in file_kepemilikan:
			if (row_milik[0] == username):
				row_milik[2] = jumlah_tiket
				
	
	for row_user in file_user:
		if (row_user[3] == username):
			row_user[6] = str(saldo)
			
	 

beli('aron01')






