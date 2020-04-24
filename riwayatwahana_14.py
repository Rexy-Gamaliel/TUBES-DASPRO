import csv
import basics

def riwayatWahana(file_pakai):
    # melihat riwayat penggunaan wahana berdasarkan input ID_Wahana
    # data dilihat berdasarkan pemakaian tiket yang tercatat pada file_pakai
    # asumsi: validasi admin/pemain dilakukan di luar fungsi
    # file_pakai = ['Username', 'Tanggal_Penggunaan', 'ID_Wahana', 'Jumlah_Tiket']
    
    # Kamus Lokal:
    # arrRiwayat: subset array file_pakai dengan ID_Wahana yang cocok dengan input
    
    ID_Wahana = input("Masukkan ID Wahana: ")
    
    # deklarasi arrRiwayat
    arrRiwayat = ['.' for i in file_pakai]    #elemen maksimal arrRiwayat adalah file_pakai
    
    # mencari dan meng-assign wahana ke arrRiwayat
    i = 0
    for data in file_pakai:
        if (data[2] == ID_Wahana):  #membandingkan komponen kedua data, yaitu ID
            arrRiwayat[i] = data
            i += 1
    # arrRiwayat berisi wahana dengan ID tertentu, namun tanggalnya masih acak
    
    # pengurutan elemen arrRiwayat berdasarkan tanggal dengan Insertion Sort
    # index yg dibandingkan adalah ID_Wahana, komponen ke-3
    arrRiwayat = basics.sort_insertion(arrRiwayat, 2)
    #arrRiwayat telah terurut
    
    #menampilkan hasil pencarian
    for baris in arrRiwayat:
        print("{} | {} | {}".format(arrRiwayat[1], arrRiwayat[0], arrRiwayat[3]))