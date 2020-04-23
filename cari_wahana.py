import csv

def cariWahana(file_wahana):
    #file_wahana: array wahana
    #file_wahana: ['ID_Wahana', 'Nama_Wahana', 'Harga_Tiket', 'Batasan_Umur', 'Batasan_Tinggi']
    #input_umur: input jenis batasan umur               valid: 1, 2, 3
    #input_tinggi: input jenis batasan tinggi badan     valid: 1, 2
    #output: Teks output hasil pencarian
    
    # User Interface: input
    print("Jenis batasan umur: ")
    print("1. Anak-anak (<17 tahun)")
    print("2. Dewasa (>= 17 tahun)")
    print("3. Semua umur")
    print()
    print("Jenis batasan tinggi badan:")
    print("1. Lebih dari 170 cm (>170)")
    print("2. Tanpa batasan")
    print()
    
    #input, validasi, dan konversi
    input_umur = input("Batasan umur pemain: ")
    while not(input_umur == "1" or input_umur == "2" or input_umur == "3"):
        print("!Batasan umur tidak valid!")
        input_umur = input("Batasan umur pemain: ")
        
    input_tinggi = input("Batasan tinggi badan: ")
    while not(input_tinggi == "1" or input_tinggi == "2"):
        print("!Batasan tinggi badan tidak valid!")
        input_tinggi = input("Batasan tinggi badan: ")
    
        #konversi input yang dimaksud ke format data dalam array
    if input_umur == '1':
        input_umur = "anak-anak"
    elif input_umur == '2':
        input_umur = "dewasa"
    elif input_umur == '3':
        input_umur = "semua umur"
    if input_tinggi == '1':
        input_tinggi = ">170"
    elif input_tinggi == '2':
        input_tinggi = "tanpa batasan"
    
    # pencarian wahana
    output = ""
    for wahana in file_wahana:
        if (wahana[3] == input_umur and wahana[4] == input_tinggi):
            output += "{} | {} | {}\n".format(wahana[0], wahana[1], wahana[2])
    
    
    # User Interface: output
    print("Hasil pencarian: ")
    if (output == ""):
        print("Tidak ada wahana yang sesuai dengan pencarian Anda.")
    else:
        print(output)