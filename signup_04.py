import password_B01

def signup(file_user):																	#fungsi sign up
	Nama = input('Masukkan nama pemain: ')
	Tanggal_Lahir = input('Masukkan tanggal lahir pemain (DD/MM/YYYY): ')
	Tinggi_Badan = input('Masukkan tinggi badan pemain (cm): ')
	Username = input('Masukkan username pemain: ')
	Password = password_B01.validasiPass()

	fields = [Nama, Tanggal_Lahir, Tinggi_Badan, Username, Password, 'Pemain', '0', 'Gray']

	for i in range (200):
		if (file_user[i][0] == '.' and file_user[i-1][0] != '.'):
			file_user[i] = fields
			break
	print('Selamat menjadi pemain, ' + str(Nama) + '. Selamat bermain.')
	return file_user
