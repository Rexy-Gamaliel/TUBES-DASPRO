import basics

def best_wahana(file_wahana, file_beli):
	# Fungsi best wahana
	# Mahasiswa diminta untuk memberikan daftar 3 wahana terbaik 
	# berdasarkan jumlah tiket yang terjual pada pemain untuk bermain 
	# di wahana terkait.
	# Format: Rank | ID Wahana | Nama Wahana | Jumlah Tiket Terjual

	ID_wahana = [0 for i in range(basics.length(file_wahana))]
	nama_wahana = [0 for i in range(basics.length(file_wahana))]
	jumlah_tiket = [0 for i in range(basics.length(file_wahana))]
	tiket_wahana = [[0 for j in range(3)] for i in range(basics.length(file_wahana))]

	for i in range(0,basics.length(file_wahana)):
		ID_wahana[i] = file_wahana[i][0]
		nama_wahana[i] = file_wahana[i][1]
		tiket_wahana[i] = [ID_wahana[i], nama_wahana[i], jumlah_tiket[i]]

	for i in range(0,basics.length(tiket_wahana)):
		for j in range(0,basics.length(file_beli)):
			if tiket_wahana[i][0]!='.' and file_beli[j][0]!='.':
				if (tiket_wahana[i][0]==file_beli[j][2]):
					tiket_wahana[i][2] = int(tiket_wahana[i][2])+int(file_beli[j][3])

	best_wahana = basics.sort_insertion_reverse(tiket_wahana,2)
	for i in range(0,3):
		print(i+1,'|',best_wahana[i][0],'|',best_wahana[i][1],'|',best_wahana[i][2])