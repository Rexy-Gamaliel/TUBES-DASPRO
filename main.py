import csv

#Fungsi Load (01)
import csv

def toArray (filename):
    f = open(filename, 'r')
    file=csv.reader(f)
    row=next(file)

    pjgkolom=0

    for field in row:
        pjgkolom+=1

    arr = [['.' for j in range (pjgkolom)] for i in range (200)]

    baris=0
    kolom=0
    print(row)
    for field in row:
        arr[baris][kolom]=field
        kolom+=1
    baris=1
    for row in file:
        kolom=0
        for field in row:
            arr[baris][kolom]=field
            kolom+=1
        baris+=1
    f.close()
    return(arr)

def load_file():
	user = input('Masukkan nama File User: ')
	file_user = toArray(user)
	wahana = input('Masukkan nama File Daftar Wahana: ')
	file_wahana = toArray(wahana)
	beli_tiket = input('Masukkan nama File Pembelian Tiket: ')
	file_beli = toArray(beli_tiket)
	guna_tiket = input('Masukkan nama File Penggunaan Tiket: ')
	file_pakai = toArray(guna_tiket)
	milik_tiket = input('Masukkan nama File Kepemilikan Tiket: ')
	file_kepemilikan = toArray(milik_tiket)
	refund = input('Masukkan nama File Refund Tiket: ')
	file_refund = toArray(refund)
	kritiksaran = input('Masukkan nama File Kritik dan Saran: ')
	file_ks = toArray(kritiksaran)
	print("File perusahaan Willy Wangky's Chocolate Factory telah di-load.")
	return(file_user, file_wahana, file_beli, file_pakai, file_kepemilikan, file_refund, file_ks)

#Fungsi Save File (02)
def fromArray(arrayname, filename):
    #Fungsi ini me-rewrite, tidak meng-append
    f = open(filename, 'w')

    for row in arrayname:
        firstField = True
        for field in row:
            if (field == '.'):
                break
            elif (firstField):
                f.write(field)
                firstField = False
            else:
                f.write(',' + field)
        if (field == '.'):
            break
        f.write('\n')

def tulisHeader(filename):


def save_file(file_user, file_wahana, file_beli, file_pakai, file_kepemilikan, file_refund, file_ks):
#   Parameter save_file() adalah nama-nama array sebagai berikut:
#	arrayname:	            filename:
#	file_user		        user
#	file_wahana		        wahana
#	file_beli	            beli_tiket
#	file_pakai	            guna_tiket
#	file_kepemilikan	    milik_tiket
#	file_refund		        refund
#	file_ks     	        kritiksaran
#   Fungsi fromArray(arrayname, filename) memindahkan data array ke csv


    user = input('Masukkan nama File User: ')
    fromArray(file_user, user)

    wahana = input('Masukkan nama File Daftar Wahana: ')
    fromArray(file_wahana, wahana)

    beli_tiket = input('Masukkan nama File Pembelian Tiket: ')
    fromArray(file_beli, beli_tiket)

    guna_tiket = input('Masukkan nama File Penggunaan Tiket: ')
    fromArray(file_pakai, guna_tiket)

    milik_tiket = input('Masukkan nama File Kepemilikan Tiket: ')
    fromArray(file_kepemilikan, milik_tiket)

    refund = input('Masukkan nama File Refund Tiket: ')
    fromArray(file_refund, refund)

    kritiksaran = input('Masukkan nama File Kritik dan Saran: ')
    fromArray(file_ks, kritiksaran)

    print("File perusahaan Willy Wangky's Chocolate Factory telah di-save.")

# Fungsi Sign Up (03)
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
	print('Selamat menjadi pemain, ' + str(Nama) + '. Selamat bermain.')

# Fungsi Login (04)
#searching user
def login_user (arrname,username,password):
    found = False
    i=0
    for row in arrname:
        if arrname[i][3]==username :
            found = True
            if arrname[i][4]==password :
                found = True
        else:
            i += 1
    return (i)

def ceklogin ():
    uname = input("Masukkan username: ")
    pas = input("Masukkan password: ")

    #hitung len array
    le = 0
    for row in file_user:
        if row[0]=='.':
            break
        else:
            le += 1

    i = login_user(file_user, uname, pas)

    while (i >= le):
        print ("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
        uname = input("Masukkan username: ")
        pas = input("Masukkan password: ")
        i = login_user(file_user, uname, pas)

    print ("Selamat bersenang-senang,",file_user[i][0],"!")
    return file_user[i]

# Fungsi Pencarian Pemain (05)
def cari_pemain():
    username = input()

    found = False
    for row in file_user:
        if row[3] == username:
            found = True
            print("Nama Pemain: " + row[0])
            print("Tinggi Pemain: " + row[2] + " cm")
            print("Tanggal Lahir Pemain: " + row[1])
            break

    if not found:
        print("Pemain tidak ditemukan")

# Fungsi Pembelian Tiket (07)
def beli(username):												
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

	tahun_sekarang = int(tanggal[-4:])
	umur = tahun_sekarang - (tahun_lahir)

	for row_wahana in file_wahana:
		if (row_wahana[0] == ID_wahana):
			nama_wahana = row_wahana[1]
			harga_tiket = int(row_wahana[2])
			total_harga = harga_tiket*jumlah_tiket
			if (saldo > total_harga):
				syarat_saldo = True
				saldo -= total_harga
			else:
				syarat_saldo = False
			if (row_wahana[4] == '>170') and (row_wahana[3]=='anak-anak'):
				if tinggi >170 and umur>=6 and umur<=12:
					syarat_tinggi = True
					syarat_umur = True
				else:
					syarat_tinggi = False
					syarat_umur = False
			elif (row_wahana[4] == '>170') and (row_wahana[3]=='dewasa'):
				if tinggi >170 and umur>=20 and umur<=45:
					syarat_tinggi = True
					syarat_umur = True
				else:
					syarat_tinggi = False
					syarat_umur = False
			else:
				syarat_tinggi = True
				syarat_umur = True

	if (syarat_tinggi==False) or (syarat_umur==False):
		print('Anda tidak memenuhi persyaratan untuk memainkan wahana ini.')
		print('Silakan menggunakan wahana lain yang tersedia.')
	elif (syarat_saldo==False):
		print('Saldo Anda tidak cukup.')
		print('Silakan mengisi saldo Anda.')
	else:
		print('Selamat bersenang-senang di '+ str(nama_wahana))
		pembelian = [username, tanggal, ID_wahana, jumlah_tiket]
		for row_beli in file_beli:
			row_beli[0] = pembelian
			break
		for row_milik in file_kepemilikan:
			if (row_milik[0] == username):
				row_milik[2] = jumlah_tiket


	for row_user in file_user:
		if (row_user[3] == username):
			row_user[6] = str(saldo)

# Fungsi Refund (09)
def refund (username_refund):
    id_wahana = input("Masukkan ID Wahana: ")
    jumlah = int(input("Jumlah: "))
    tanggal = input("Masukkan tanggal hari ini: ")
    found = False
    i=0 #Untuk tahu row berapa di file_kepemilikan

    for row in file_kepemilikan:
        if row[0] == username_refund and row[1] == id_wahana:
            found=True
            if jumlah <= int(row[2]):
                temp=int(row[2])-jumlah
                if temp==0:
                    j=1
                    while (file_kepemilikan[i+j][0]!='.'):
                        file_kepemilikan[i]=file_kepemilikan[i+j]
                        j+=1
                    file_kepemilikan[i]=['.','.','.','.','.','.','.']
                else:
                    file_kepemilikan[i][2]=temp
                for row_wahana in file_wahana:
                    if id_wahana == row_wahana[0]:
                        price = int(row_wahana[2])
                j=0
                for row_user in file_user:
                    if username_refund == row_user[3]:
                        temp=int(row_user[6])
                        temp+=price*jumlah
                        row_user[6]=str(temp)
                        file_user[j]=row_user
                        break
                    j+=1
                print("Refund berhasil. Saldo anda sekarang " + row_user[6])
                j=0
                for row_refund in file_refund:
                    if(row_refund[0]=="."):
                        file_refund[j][0]=username_refund
                        file_refund[j][1]=tanggal
                        file_refund[j][2]=id_wahana
                        file_refund[j][3]=jumlah
                    break
                    j+=1
            else:
                print("Anda hanya memiliki " + row[2] + " tiket untuk wahana ini.")
            i+=1
            break

    if not found:
        print("Anda tidak memiliki tiket wahana ini.")

# Fungsi Top Up Saldo (13)
def topup():
    username=input("Masukkan username: ")
    topup=int(input("Masukkan saldo yang di-top up: "))
    found = False
    i=0
    for row in file_user:
        if row[3] == username:
            found = True
            row[6]= str(int(row[6]) + topup)
            file_user[i]=row
            print("Top up berhasil. Saldo " + str(row[0]) + " bertambah menjadi " + str(row[6]))
        i+=1
    if not found:
      print("Pemain tidak ditemukan")

#Fungsi Utama
loggedin=False

(file_user, file_wahana, file_beli, file_pakai, file_kepemilikan, file_refund, file_ks) = load_file()
keluarprogram=False
while not keluarprogram:
    print()
    print("=====================================================================")
    print("         SELAMAT DATANG DI WAHANA BERMAIN WILLY WANGKY")
    print("=====================================================================")
    print()
    if (loggedin==False):
        print("Apa yang akan Anda lakukan hari ini? ")
        print()
        print("Menu:")
        print("1. Login User")
        print("2. Save File")
        print()
        menu=input()
        print()
        valid=False
        while not valid:
            if(menu=="1"):
                user_info=ceklogin()
                valid=True
                loggedin=True
            elif(menu=="1"):
                valid=True
            else:
                print("Ups, menu yang kamu pilih tidak ada!")

    elif (user_info[5] == "Admin"):
        print("Hi, " + user_info[0] +"!")
        print()
        print("Apa yang akan Anda lakukan hari ini? ")
        print()
        print("Menu:")
        print("1. Sign Up User")
        print("2. Pencarian Pemain")
        print("3. Pencarian Wahana")
        print("4. Lihat Kritik dan Saran")
        print("5. Menambahkan Wahana Baru")
        print("6. Top Up Saldo")
        print("7. Lihat Riwayat Penggunaan Wahana")
        print("8. Lihat Jumlah Tiket Pemain")
        print("9. Save File")
        print("0. Exit")
        print()
        menu=input()
        print()
        if (menu=="1"):
            signup()
        elif (menu=="2"):
            cari_pemain()
        elif (menu=="3"):
            x=True
        elif (menu=="4"):
            x=True
        elif (menu=="5"):
            x=True
        elif (menu=="6"):
            topup()
        elif (menu=="7"):
            x=True
        elif (menu=="8"):
            x=True
        elif (menu=="9"):
            save_file(file_user, file_wahana, file_beli, file_pakai, file_kepemilikan, file_refund, file_ks)
        elif (menu=="0"):
            keluarprogram=True
        else:
            print("Ups, menu yang kamu pilih tidak ada!")

    else:
        print("Hi, " + user_info[0] +"!")
        print()
        print("Apa yang akan Anda lakukan hari ini? ")
        print()
        print("Menu:")
        print("1. Cari Wahana")
        print("2. Beli Tiket")
        print("3. Naik Wahana") #Menggunakan tiket
        print("4. Refund Tiket")
        print("5. Kritik dan Saran")
        print("6. Save File")
        print("0. Exit")
        print()
        menu=input()
        print()
        if (menu=="1"):
            x=True
        elif (menu=="2"):
            beli_tiket(user_info[3])
        elif (menu=="3"):
            x=True
        elif (menu=="4"):
            refund(user_info[3])
        elif (menu=="5"):
            x=True
        elif (menu=="6"):
            save_file(file_user, file_wahana, file_beli, file_pakai, file_kepemilikan, file_refund, file_ks)
        elif (menu=="0"):
            keluarprogram=True
        else:
            print("Ups, menu yang kamu pilih tidak ada!")
