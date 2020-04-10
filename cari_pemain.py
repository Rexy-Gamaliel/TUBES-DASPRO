def cari_pemain():
	username = input("Masukkan username: ")
	for row in user_file:
		for field in row:
			if field == username:
				print("Nama Pemain: " + row[0])
				print("Tinggi Pemain: " + row[2] + " cm")
				print("Tanggal Lahir Pemain: " + row[1])
        
## Program utama
cari_pemain()
