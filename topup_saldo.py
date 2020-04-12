def topup_saldo():
	username=input("Masukkan username: ")
	topup=int(input("Masukkan saldo yang di-top up: "))
	found = False
	for row in user_file:
		if row[3] == username:
			found = True
			temp=int(row[6]) + topup
			row[6]= int(row[6]) + topup
			print("Top up berhasil. Saldo " + str(row[0]) + " bertambah menjadi " + str(row[6]))
	if not found:
		print("Pemain tidak ditemukan")

## Program utama
topup_saldo()
