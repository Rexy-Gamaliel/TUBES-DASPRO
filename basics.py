# Ini isinya fungsi-fungsi dasar
# import dulu sebelum pakai
# Jangan lupa makai fungsinya pakai syntax basics.namafungsi()

def length(array):
    # Menghitung banyak data dalam array
    # EOP: mark berupa '.'
    # Semua array hasil load diasumsikan memiliki elemen berupa array
    # dan mengandung setidaknya mark
    count = 0
    for baris in array:
        count += 1
        if (baris[0] == '.'):
            break
    return count

def sort_insertion(array, idxBanding):
    # Sorting: Insertion (ascending)
    # Untuk proses insertion ke-Pass (Pass [1,N-1]), akan dicari
    # posisi yang tepat untuk elemen ke-Pass dengan membandingkannya
    # dengan elemen terurut [0, Pass-1], dimulai dari Pass-1
    # Perbandingan dilihat dari komponen ke-idxBanding dari elemen array
    # (karena file array semuanya menyerupai tipe bentukan, atau matriks
    # berukuran 2x2)

    # KAMUS
    # Pass  : proses insertion keberapa
    # Temp  : menyimpan sementara nilai elemen ke-Pass
    # idxBanding: index komponen dari elemen array yg akan dibandingkan
    N = length(array)
    
    for Pass in range(1,N):     #Pass dari 1 sampai N-1
        Temp = array[Pass]
        #Akan dibandingkan nilai Temp dengan array[i], untuk i [0, Pass-1]
        i = Pass - 1
        while (Temp[idxBanding] < array[i][idxBanding] and i >= 0):
            array[i+1] = array[i]   #elemen terurut digeser
            i -= 1                  #pembandingan digeser ke depan
        #Temp[idxBanding] >= array[i][idxBanding] atau i = 0 (Temp adalah elemen terkecil)

        array[i+1] = Temp   #karena saat keluar loop i yang tepat telah berkurang 1
    
    return(array)

def sort_insertion_reverse(array, idxBanding):
    # Sorting: Insertion (descending)
    # Sama persis dengan fungsi sort_insertion di atas, namun descending
    
    # KAMUS
    # Pass  : proses insertion keberapa
    # Temp  : menyimpan sementara nilai elemen ke-Pass
    # idxBanding: index komponen dari elemen array yg akan dibandingkan
    N = length(array)
    
    for Pass in range(1,N):     #Pass dari 1 sampai N-1
        Temp = array[Pass]
        #Akan dibandingkan nilai Temp dengan array[i], untuk i [0, Pass-1]
        i = Pass - 1
        while (Temp[idxBanding] > array[i][idxBanding] and i >= 0):
            array[i+1] = array[i]   #elemen terurut digeser
            i -= 1                  #pembandingan digeser ke depan
        #Temp[idxBanding] >= array[i][idxBanding] atau i = 0 (Temp adalah elemen terkecil)

        array[i+1] = Temp   #karena saat keluar loop i yang tepat telah berkurang 1
    
    return(array)


def delete_row(i, arrname, leng):
    # i = index awal array yang akan di-delete
    # leng = panjang array
    
    for j in range(i+1, leng):
        arrname[j-1] = arrname[j]
    arrname[leng] = ['.']
