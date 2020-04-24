def signup(file_user):																	#fungsi sign up
	Nama = input('Masukkan nama pemain: ')
	Tanggal_Lahir = input('Masukkan tanggal lahir pemain (DD/MM/YYYY): ')
	Tinggi_Badan = input('Masukkan tinggi badan pemain (cm): ')
	Username = input('Masukkan username pemain: ')
	Password = input('Masukkan password pemain: ')

	fields = [Nama, Tanggal_Lahir, Tinggi_Badan, Username, Password, 'Pemain', '0']

	for i in range (200):
		if (file_user[i][0] == '.' and file_user[i-1][0] != '.'):
			file_user[i] = fields
			break
	print('Selamat menjadi pemain, ' + str(Nama) + '. Selamat bermain.')
	return file_user
