import csv
import load_01
import login_02
import save_03
import signup_04
import caripemain_05
import cariwahana_06
import belitiket_07
import gunatiket_08
import refund_09
import kritiksaran_10
import lihatks_11
import tambahwahana_12
import topup_13
import riwayatwahana_14
import lihattiket_15
import keluar_16
import password_B01
import upgrade_B02
import bestwahana_B03
import laporhilang_B04

#Fungsi Utama
loggedin=False

# load file
(file_user, file_wahana, file_beli, file_pakai, file_kepemilikan, file_refund, file_ks, file_kehilangan) = load_01.load_file()

keluarprogram=False
loggedin=False

# Selama user belum menjalankan menu exit, fungsi akan terus looping
while not keluarprogram:
    print()
    print("=====================================================================")
    print()
    print("         SELAMAT DATANG DI WAHANA BERMAIN WILLY WANGKY")
    print()
    print("=====================================================================")
    print()

    if not loggedin:
        user_info=login_02.ceklogin(file_user)
        loggedin=True

    elif (user_info[5] == "Admin"): #Menu apabila user adalah admin
        print("Hi, {} !".format(user_info[0]))
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
        print("10. Upgrade akun")
        print("11. Lihat Wahana terbaik")
        print("0. Exit")
        print()
        menu=input(">>> ")
        print()
        if (menu=="1"):
            file_user = signup_04.signup(file_user)
        elif (menu=="2"):
            caripemain_05.cari_pemain(file_user)
        elif (menu=="3"):
            cariwahana_06.cariWahana(file_wahana)
        elif (menu=="4"):
            lihatks_11.lihat_laporan(file_ks)
        elif (menu=="5"):
            file_wahana = tambahwahana_12.tambah_wahana(file_wahana)
        elif (menu=="6"):
            file_user = topup_13.topup(file_user)
        elif (menu=="7"):
            riwayatwahana_14.riwayatWahana(file_user)
        elif (menu=="8"):
            lihattiket_15.tiket_pemain(file_kepemilikan, file_wahana)
        elif (menu=="9"):
            save_03.save_file(file_user, file_wahana, file_beli, file_pakai, file_kepemilikan, file_refund, file_ks, file_kehilangan)
        elif(menu=="10"):
            file_user = upgrade_B02.upgradeakun(file_user)
        elif(menu=="11"):
            bestwahana_B03.best_wahana(file_wahana, file_beli)
        elif (menu=="0"):
            keluarprogram = keluar_16.exit(file_user, file_wahana, file_beli, file_pakai, file_kepemilikan, file_refund, file_ks, file_kehilangan)
        else:
            print("Ups, menu yang kamu pilih tidak ada!")

    else:   #Menu apabila user adalah pemain
        print("Hi, {} !".format(user_info[0]))
        print()
        print("Apa yang akan Anda lakukan hari ini? ")
        print()
        print("Menu:")
        print("1. Cari Wahana")
        print("2. Beli Tiket")
        print("3. Naik Wahana")
        print("4. Refund Tiket")
        print("5. Kritik dan Saran")
        print("6. Save File")
        print("0. Exit")
        print()
        menu=input(">>> ")
        print()
        if (menu=="1"):
            cariwahana_06.cariWahana(file_wahana)
        elif (menu=="2"):
            (file_user, file_beli, file_kepemilikan) = belitiket_07.beli(user_info[3], file_user, file_wahana, file_beli, file_kepemilikan)
        elif (menu=="3"):
            (file_kepemilikan, file_pakai) = gunatiket_08.guna_tiket(user_info[3], file_kepemilikan, file_pakai)
        elif (menu=="4"):
            (file_user, file_kepemilikan, file_refund) = refund_09.refund(user_info[3], file_user, file_kepemilikan, file_wahana, file_refund)
        elif (menu=="5"):
            file_ks = kritiksaran_10.tulisKritikSaran(user_info[3], file_ks)
        elif (menu=="6"):
            save_03.save_file(file_user, file_wahana, file_beli, file_pakai, file_kepemilikan, file_refund, file_ks, file_kehilangan)
        elif (menu=="0"):
            keluarprogram = keluar_16.exit(file_user, file_wahana, file_beli, file_pakai, file_kepemilikan, file_refund, file_ks, file_kehilangan)
        else:
            print("Ups, menu yang kamu pilih tidak ada!")
    input()