def cari_pemain():
	username = input("Masukkan username: ")
	found = False
	for row in user_file:
		for field in row:
			if field == username:
				found = True
				print("Nama Pemain: " + row[0])
				print("Tinggi Pemain: " + row[2] + " cm")
				print("Tanggal Lahir Pemain: " + row[1])
	if not found:
		print("Pemain tidak ditemukan")
        
## Program utama
cari_pemain()
