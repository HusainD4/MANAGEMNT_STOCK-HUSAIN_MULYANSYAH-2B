def menu ():
    print('='*25)
    print ('1. Tambah Data Barang')
    print ('2. Edit Data')
    print ('3. Hapus Data Barang')
    print ('4. Cari Barang')
    print ('5. Tampilkan Data Barang')
    print ('6. Tampilkan Jumlah Data')
    print ('7. Keluar')
    print('='*25)


barang = []
def tambah ():
    nama = input('Masukan Nama Barang : ')
    stok = input('Masukan Stok Barang : ')
    data_baru = {'nama barang':nama,'stok':stok}
    barang.append(data_baru)

def edit():
    nomor_barang = int(input("Hapus Data Barang ke : "))
    if 1 <= nomor_barang <= len(barang):
        nomor_index = nomor_barang - 1
        item = barang[nomor_index]
        item['nama'] = input("Masukkan nama barang baru: ")
        item['stok'] = int(input("Masukkan stok barang baru: "))
        print("Data barang berhasil diubah.")
    else:
        print("Nomor barang tidak ditemukan.")


def delete():
    hapus = int(input('Hapus Data Index Ke : '))
    if barang:
        if 1 <= hapus <= len(barang):
            del barang[hapus - 1]
            print("Data barang berhasil dihapus.")
        else:
            print("Index barang tidak ditemukan.")
    else:
        print('Data barang kosong.')

def cari_data():
    if barang:
        kata = input("Cari Nama Barang: ")
        ditemukan = False
        for item in barang:
            if kata.lower() in item['nama barang'].lower():
                print("=== HASIL PENCARIAN ===")
                print(f"- {item['nama barang']} stock {item['stok']}")
                ditemukan = True
        if not ditemukan:
            print("Barang tidak ditemukan.")
    else:
        print("Barang tidak ditemukan.")

def data_barang():
    print("= = = = = T o k o E l e k t r o n i k = = = = =")
    if barang:
        print("=== DATA BARANG ==")
        for item in barang:
            print(f"- {item['nama barang']} stock {item['stok']}")
    else:
        print("=== DATA BARANG KOSONG ===")

def tampilkan_jumlah_data_barang():
    print(f"Jumlah Data Tersimpan: {len(barang)} Barang")


