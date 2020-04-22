# Function Sign Up USer
# Pendaftaran pemain hanya dapat dilakukan oleh admin dan 
# tidak diizinkan memasukkan username yang sudah terdaftar

# Kamus
# Nama, Tanggal_Lahir, Tinggi_Badan, Username, Password, role : str
# fields : list

#Algoritma

import csv

def toArray (filename):											#kalau udah digabung, fungsi toArraynya boleh dihapus
	f = open(filename, 'r')
	file=csv.reader(f)
	row=next(file)

	arr = [['.' for j in range (7)] for i in range (200)]

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
	
user = input('Masukkan nama File User: ')
file_user = toArray(user)

def signup():																	#fungsi sign up
	Nama = input('Masukkan nama pemain: ')
	Tanggal_Lahir = input('Masukkan tanggal lahir pemain (DD/MM/YYYY): ')
	Tinggi_Badan = input('Masukkan tinggi badan pemain (cm): ')
	Username = input('Masukkan username pemain: ')				
	Password = input('Masukkan password pemain: ')

	fields = [Nama, Tanggal_Lahir, Tinggi_Badan, Username, Password, 'Pemain', '0']
	
	for i in range (100,200):
		if (file_user[i][0] == '.' and file_user[i-1][0] != '.'):
			file_user[i] = fields
			break
