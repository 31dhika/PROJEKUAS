#mengakses modul
from datetime import datetime
saat_ini = datetime.now()
tgl_jam = saat_ini.strftime("%d-%m-%Y %H:%M:%S") # format dd/mm/YY H:M:S 

#mengakses modul
from prettytable import PrettyTable
x = PrettyTable()

#tabel untuk menu
x.field_names = ("NO","PAKAIAN","UKURAN","HARGA")
x.add_row(["1","Kemeja","M-XL","Rp.100K"])
x.add_row(["2","Kaos lengan pendek","M-XL","Rp.75K"])
x.add_row(["3","Kaos lengan panjang","M-XL","Rp.80K"])
x.add_row(["4","Celana jeans","39-41","Rp.125k"])

print(x)

#variabel list
kode = []
ukuran = []
merk = []
harga = []
jmlhpotong = []
jmlhharga = []

banyakjenis = int(input("Banyak jenis : "))#untuk menentukan berapa banyak perulangan

#input dan logika if
def proses() :
    global jmlhpotong
    global harga
    for i in range(banyakjenis):
        print ("Jenis Ke - " + str(i+1))
        kode.append(int(input("\tSilahkan masukan pilihan anda dengan angka [1-4] : ")))
        ukuran.append(input("\tSilahkan pilih ukurannya\t : "))
        jmlhpotong.append(int(input("\tBerapa potong yang ingin di beli : ")))
        if kode[i] == "1" :
            merk.append("Kemeja")
            if ukuran == "m" or ukuran == "M" :
                harga.append(100000)
            elif ukuran == "l" or ukuran == "L" :
                harga.append(100000)
            else : 
                ukuran == "xl" or ukuran == "Xl"
                harga.append(100000)
        elif kode[i] == "2" :
            merk.append("Kaos lengan pendek")
            if ukuran == "m" or ukuran == "M" :
                harga.append(75000)
            elif ukuran == "l" or ukuran == "L" :
                harga.append(75000)
            else : 
                ukuran == "xl" or ukuran == "Xl"
                harga.append(75000)
        elif kode[i] == "3" :
            merk.append("Kaos lengan panjang")
            if ukuran == "m" or ukuran == "M" :
                harga.append(80000)
            elif ukuran == "l" or ukuran == "L" :
                harga.append(80000)
            else : 
                ukuran == "xl" or ukuran == "Xl"
                harga.append(80000)
        elif kode[i] == "4" :
            merk.append("Celana Jeans")
            if ukuran == "39" :
                harga.append(150000)
            elif ukuran == "40" :
                harga.append(150000)
            else : 
                ukuran == "41"
                harga.append(150000)
        else :
            ukuran.append("\t\tANDA SALAH MEMASUKAN NO PILIHAN")
            harga.append(0)
    jumbay = []
    for i in range(banyakjenis) :
        jmlhharga.append(harga[i]*jmlhpotong[i])
        jumbay = jmlhharga
    print("Total\t\t   :",jmlhharga)
    ubay = int(input("masukan uang bayar : "))
    uangkembali = (ubay-jumbay)
    print("uang kembali\t   :",uangkembali)
    print("----------------------------------------------")

proses()




""""
#jika ingin pesan lagi
def tanya() :
    tanya = input("Ingin pesan lagi (y/t) ? : ")
    if tanya == "y" :
        proses()
        hitung()
    elif tanya == "t" :
        struk()
    else :
        print("Masukan input yang benar")
    return
tanya()
"""

#output

""""
def struk() :
    print("\t\tJ-Da\'an clothes")
    print("\tJl. Raya Halim kusuma no. 18")
    print("\t\tTelp/wa 0899999")
    print("----------------------------------------------")
    print("\t     ",tgl_jam)
    print("----------------------------------------------")
    print("Perhitungan barang yang dibeli")
    print("----------------------------------------------")
    print("\t\t\tTotal   : ",harga)
    print("\t\t\tBayar   : ",ubay)
    print("\t\t\tKembali : ",uangkembali)
    print("----------------------------------------------")
    print("\t\tTERIMAKASIH")
    print("\t   SELAMAT BELANJA KEMBALI")

struk()
"""
