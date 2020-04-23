import csv

def tulisKritikSaran(Username, file_ks):
    # Menuliskan input user ke array file_ks
    
    # file_ks = ['Username', 'Tanggal_Kritik', 'ID_Wahana', 'Isi_Kritik']
    
    # User Interface: input
    inputIDWahana = input("Masukkan ID Wahana: ")
    inputTanggalKritik = input("Masukkan tanggal pelaporan: ")
    inputIsiKritik = input("Kritik atau sarana Anda: ")
    
    # Menuliskan kritik dan saran ke array
    for baris in file_ks:
        if (baris[0] == '.'):     #mencari baris kosong
            baris[0] = Username 
            baris[1] = inputTanggalKritik
            baris[2] = inputIDWahana
            baris[3] = inputIsiKritik
            break
    
    # User Interface: output
    print("Kritik dan saran Anda kami terima. Terima Kasih!")