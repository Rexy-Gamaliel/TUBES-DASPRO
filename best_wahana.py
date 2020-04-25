# Fungsi best wahana
# Mahasiswa diminta untuk memberikan daftar 3 wahana terbaik 
# berdasarkan jumlah tiket yang terjual pada pemain untuk bermain 
# di wahana terkait.
# Format: Rank | ID Wahana | Nama Wahana | Jumlah Tiket Terjual

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

beli_tiket = input('Masukkan nama File Pembelian Tiket: ')
file_beli = toArray(beli_tiket)
wahana = input('Masukkan nama File Daftar Wahana: ')
file_wahana = toArray(wahana)

def length(array):
    # Menghitung banyak data dalam array
    # EOP: mark berupa '.'
    # EOF: mark berupa '*'
    # Semua array hasil load diasumsikan memiliki elemen berupa array
    # dan mengandung setidaknya mark
    count = 0
    for baris in array:
        count += 1
        if (baris[0] == '.') or (baris[0] == '*'):
            break
    return count
    
def reverseInsertionSort(arr, a):
	for i in range(1, length(arr)):
		key = arr[i][a]
		elem = arr[i]
		j = i-1
		while j>=0 and key>arr[j][a]:
			arr[j+1] = arr[j]
			j-=1
		arr[j+1]=elem
	return(arr)

def best_wahana():
	ID_wahana = [0 for i in range(length(file_wahana))]
	nama_wahana = [0 for i in range(length(file_wahana))]
	jumlah_tiket = [0 for i in range(length(file_wahana))]
	tiket_wahana = [[0 for j in range(3)] for i in range(length(file_wahana))]

	for i in range(0,length(file_wahana)):
		ID_wahana[i] = file_wahana[i][0]
		nama_wahana[i] = file_wahana[i][1]
		tiket_wahana[i] = [ID_wahana[i], nama_wahana[i], jumlah_tiket[i]]

	for i in range(0,length(tiket_wahana)):
		for j in range(0,length(file_beli)):
			if tiket_wahana[i][0]!='.' and file_beli[j][0]!='.':
				if (tiket_wahana[i][0]==file_beli[j][2]):
					tiket_wahana[i][2] = int(tiket_wahana[i][2])+int(file_beli[j][3])

	best_wahana = reverseInsertionSort(tiket_wahana,2)
	for i in range(0,3):
		print(i+1,'|',best_wahana[i][0],'|',best_wahana[i][1],'|',best_wahana[i][2])
best_wahana()
