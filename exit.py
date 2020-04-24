import load
import save

def exit ():
    file_user = load.toArray ("user.csv")
    file_wahana = load.toArray ("wahana.csv")
    file_beli = load.toArray ("pembelian.csv")
    file_pakai = load.toArray ("penggunaan.csv")
    file_kepemilikan = load.toArray ("kepemilikan_tiket.csv")
    file_refund = load.toArray ("refund_tiket.csv")
    file_ks = load.toArray ("kritik_dan_saran.csv")

    keluar = input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N)? ")

    if keluar=="Y" :
        save.save_file(file_user, file_wahana, file_beli, file_pakai, file_kepemilikan, file_refund, file_ks)
        
exit()
