def validasiPass():
    # Memastikan keamanan password user dengan memvalidasi password
    # lalu melakukan hashing. Meminta password kepada user hingga valid
    # Ketentuan password:
    # 1. Mengandung angka, char huruf Kapital dan kecil
    # 2. Minimal terdiri atas 4 karakter
    # Validasi karakter pada pw dilakukan menggunakan fungsir ord()
    # dengan melihat daftar kode pada unicode.
    # A-Z: 65-90, a-z: 97-122, 0-9: 48-57
    #
    # CONTOH PENGGUNAAN PADA FUNGSI SIGNUP():
    # password = password_B01.validasiPass()
    #
    # valid: array of boolean untuk memvalidasi keempat syarat di atas,
    # berturut-turut yaitu: HURUF KAPITAL, huruf kecil, angka, panjang pw
    # promptPass: boolean, untuk memastikan password sebelum prosedur berakhir
    
    promptPass = True
    
    while (promptPass):
        pw = input("Masukkan password pemain: ")
        
        valid = [False, False, False, False]
        panjangPW = 0
        
        pw = str(pw)
        
        for char in pw:
            panjangPW += 1
            # validasi huruf kapital
            if (ord(char) >= 65 and ord(char) <= 90):
                valid[0] = True
            # validasi huruf kecil
            elif (ord(char) >= 97 and ord(char) <= 122):
                valid[1] = True
            # validasi angka
            elif (ord(char) >= 48 and ord(char) <= 57):
                valid[2] = True
        # validasi panjang password
        if (panjangPW >= 4):
            valid[3] = True
        
        if (valid[0] == True and valid[1] == True and valid[2] == True and valid[3] == True):
            promptPass = False
            return hash(pw)
        else:
            print("Password Anda tidak sesuai ketentuan.")