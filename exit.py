import save

def exit (file_user, file_wahana, file_beli, file_pakai, file_kepemilikan, file_refund, file_ks):
    #Memproses apabila input user adalah Y
    keluar = input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N)? ")

    if keluar=="Y" :
        save.save_file(file_user, file_wahana, file_beli, file_pakai, file_kepemilikan, file_refund, file_ks)
    return()
