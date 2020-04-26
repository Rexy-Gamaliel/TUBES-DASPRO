import save_03

def exit (file_user, file_wahana, file_beli, file_pakai, file_kepemilikan, file_refund, file_ks, file_kehilangan):
    # Mengambil input Y/N
    keluar = input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N)? ")

    # Jika input Y maka akan menjalankan fungsi save file
    if keluar=="Y" :
        save_03.save_file(file_user, file_wahana, file_beli, file_pakai, file_kepemilikan, file_refund, file_ks, file_kehilangan)
    return(True)
