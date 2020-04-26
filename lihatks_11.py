import basics


def lihat_laporan(file_ks):
	print('Kritik dan saran:')
	file_ks2 = basics.sort_insertion(file_ks, 2)
	for row in file_ks2:
		if(row[2]!='.' and row[2] != '*' and row[0] != 'Username'):
			print(row[2],'|',row[1],'|',row[0],'|',row[3])