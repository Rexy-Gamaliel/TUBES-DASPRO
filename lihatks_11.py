import basics

def insertionSort(arr, a):
	for i in range(1, basics.length(arr)):
		key = arr[i][a]
		elem = arr[i]
		j = i-1
		while j>=0 and key<arr[j][a]:
			arr[j+1] = arr[j]
			j-=1
		arr[j+1]=elem
	return(arr)

def lihat_laporan(file_ks):
	print('Kritik dan saran:')
	file_ks2 = insertionSort(file_ks, 2)
	for row in file_ks2:
		if(row[2]!='.' and row[2] != '*' and row[0] != 'Username'):
			print(row[2],'|',row[1],'|',row[0],'|',row[3])
