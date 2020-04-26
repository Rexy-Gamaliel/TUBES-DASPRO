import basics

def beli(username, file_user, file_wahana, file_beli, file_kepemilikan):
	# Pembelian tiket hanya dapat dilakukan oleh pemain yang telah terdaftar dan melakukan login
	# Kamus
	# ID_wahana, tanggal, nama_wahana, tanggal_lahir: str
	# jumlah_tiket, tinggi, saldo, umur, harga_tiket, total_harga : int
	# tahun_lahir, tahun_sekarang : int
	# syarat_tinggi, syarat_umur, syarat_saldo : bool

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
			jenisakun = row_user[7]
			
	tahun_sekarang = int(tanggal[-4:])
	umur = tahun_sekarang - (tahun_lahir)
	
	for i in range(0, basics.length(file_wahana)):	#penentuan syarat wahana
		if (file_wahana[i][0] == ID_wahana):
			nama_wahana = file_wahana[i][1]
			harga_tiket = int(file_wahana[i][2])
			if (jenisakun == "Gold"): # Bagian dari spesifikasi bonus akun gold
				harga_tiket = harga_tiket//2
			total_harga = harga_tiket*int(jumlah_tiket)
			if (saldo > total_harga):
				syarat_saldo = True
			else:
				syarat_saldo = False
			if (file_wahana[i][4] == '>170') and (file_wahana[i][3]=='anak-anak'):
				if tinggi >170 and umur<17:
					syarat_tinggi = True
					syarat_umur = True
				else:
					syarat_tinggi = False
					syarat_umur = False
			elif (file_wahana[i][4] == '>170') and (file_wahana[i][3]=='dewasa'):
				if tinggi >170 and umur>=17:
					syarat_tinggi = True
					syarat_umur = True
				else:
					syarat_tinggi = False
					syarat_umur = False
			else:
				syarat_tinggi = True
				syarat_umur = True
	
	if (syarat_tinggi==False) or (syarat_umur==False):		   #mencetak pesan sesuai keadaaan yang terpenuhi
		print('Anda tidak memenuhi persyaratan untuk memainkan wahana ini.')
		print('Silakan menggunakan wahana lain yang tersedia.')
	elif (syarat_saldo==False):
		print('Saldo Anda tidak cukup.')
		print('Silakan mengisi saldo Anda.')
	else:
		print('Selamat bersenang-senang di '+ str(nama_wahana))
		saldo-=total_harga
		pembelian = [username, tanggal, ID_wahana, jumlah_tiket]
		for i in range(0, basics.length(file_beli)):				#menambah data ke file pembelian
			if file_beli[i][0] != '.':
				file_beli[i] = pembelian
				break
		kepemilikan = [username, ID_wahana, jumlah_tiket]
		for i in range(0,basics.length(file_kepemilikan)): 		#menambah data ke file kepemilikan tiket
			if (file_kepemilikan[i][0] == username):        #INI YANG REXY BENERIN:
				if (file_kepemilikan[i][1] == ID_wahana):          #kasus jika username sudah ada
					file_kepemilikan[i][2] += kepemilikan[2]        #khususnya, jika sudah punya tiket di wahana yg sama
			elif (file_kepemilikan[i][0] == '.'):               #kasus jika belum punya tiket di wahana tsb sebelumnya
				file_kepemilikan[i] = kepemilikan
	for i in range(0,basics.length(file_user)):
		if (file_user[i][3] == username):
			file_user[i][6] = str(saldo)

	return(file_user, file_beli, file_kepemilikan)
