def load_file():  
  user = input('Masukkan nama File User: ')
	wahana = input('Masukkan nama File Daftar Wahana: ')
	beli_tiket = input('Masukkan nama File Pembelian Tiket: ')
	guna_tiket = input('Masukkan nama File Penggunaan Tiket: ')
	milik_tiket = input('Masukkan nama File Kepemilikan Tiket: ')
	refund = input('Masukkan nama File Refund Tiket: ')
	kritiksaran = input('Masukkan nama File Kritik dan Saran: ')

	user_file = csv.reader(open(user, 'r'))
	wahana_file = csv.reader(open(wahana, 'r'))
	beli_tiket_file = csv.reader(open(beli_tiket, 'r'))
	guna_tiket_file = csv.reader(open(guna_tiket, 'r'))
	milik_tiket_file = csv.reader(open(milik_tiket, 'r'))
	refund_file = csv.reader(open(refund, 'r'))
	kritiksaran_file = csv.reader(open(kritiksaran, 'r'))

	print("File perusahaan Willy Wangky's Chocolate Factory telah di-load")
