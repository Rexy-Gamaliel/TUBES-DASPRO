def cari_pemain():
    username = input()

    found = False
    for row in file_user:
        if row[3] == username:
            found = True
            print("Nama Pemain: " + row[0])
            print("Tinggi Pemain: " + row[2] + " cm")
            print("Tanggal Lahir Pemain: " + row[1])

    if not found:
        print("Pemain tidak ditemukan")
