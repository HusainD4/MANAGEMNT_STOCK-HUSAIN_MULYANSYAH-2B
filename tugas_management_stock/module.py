import manage as mg

while True:
    mg.menu()
    pilihan = int(input('Masukan Pilihan : '))

    if pilihan == 1:
        mg.tambah()
    if pilihan == 2:
        mg.edit()
    if pilihan == 3:
        mg.delete()
    if pilihan == 4:
        mg.cari_data()
    if pilihan == 5:
        mg.data_barang()
    if pilihan == 6:
        mg.tampilkan_jumlah_data_barang()
    if pilihan == 7:
        print('='*25)  
        print("TERIMAKASIH TELAH MENGGUNAKAN PROGRAM\nDATA MANAGEMENT HUSAIN")  
        print('='*25)
        exit()  
