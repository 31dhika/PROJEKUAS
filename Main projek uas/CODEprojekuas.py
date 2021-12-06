#mengakses modul
from datetime import datetime
saat_ini = datetime.now()
tgl_jam = saat_ini.strftime("%d-%m-%Y %H:%M:%S") # format dd/mm/YY H:M:S 

#mengakses modul
import pandas as pd

#mengakses modul
from prettytable import PrettyTable
x = PrettyTable()

#tabel untuk menu
x.field_names = ("NO","PAKAIAN","UKURAN","HARGA")
x.add_row(["1","Kemeja","M-XL","Rp.100K"])
x.add_row(["2","Kaos lengan pendek","M-XL","Rp.75K"])
x.add_row(["3","Kaos lengan panjang","M-XL","Rp.80K"])
x.add_row(["4","Celana jeans","39-41","Rp.150k"])

print(x)

#variabel list
kode = []
ukuran = []
merk = []
harga = []
jmlhpotong = []
jmlhharga = []

banyakjenis = int(input("Masukan banyak jenis pembelian : "))#untuk menentukan berapa banyak perulangan

# perulangan,input dan logika if
class mulai :
    def proses() :
        global jmlhpotong
        global harga
        global merk
        for i in range(banyakjenis):
            print ("Jenis Ke - " + str(i+1))
            kode.append(int(input("\tSilahkan masukan pilihan anda dengan angka [1-4] : ")))
            ukuran.append(input("\tSilahkan pilih ukurannya\t : "))
            jmlhpotong.append(int(input("\tBerapa potong yang ingin di beli : ")))
            if kode[i] == 1 :
                merk.append("Kemeja")
                if ukuran[i] == "m" or ukuran[i] == "M" :
                    harga.append(100000)
                elif ukuran[i] == "l" or ukuran[i] == "L" :
                    harga.append(100000)
                elif ukuran[i] == "xl" or ukuran[i] == "XL" :
                    harga.append(100000)
                else :
                    print("Ukuran tidak tersedia")
                    harga.append(0)
            elif kode[i] == 2 :
                merk.append("Kaos lengan pendek")
                if ukuran[i] == "m" or ukuran[i] == "M" :
                    harga.append(75000)
                elif ukuran[i] == "l" or ukuran[i] == "L" :
                    harga.append(75000)
                elif ukuran[i] == "xl" or ukuran[i] == "XL" :
                    harga.append(75000)
                else :
                    print("Ukuran tidak tersedia")
                    harga.append(0)
            elif kode[i] == 3 :
                merk.append("Kaos lengan panjang")
                if ukuran[i] == "m" or ukuran[i] == "M" :
                    harga.append(80000)
                elif ukuran[i] == "l" or ukuran[i] == "L" :
                    harga.append(80000) 
                elif ukuran[i] == "xl" or ukuran[i] == "XL" :
                    harga.append(80000)
                else :
                    print("Ukuran tidak tersedia")
                    harga.append(0)
            elif kode[i] == 4 :
                merk.append("Celana Jeans")
                if ukuran[i] == "39" :
                    harga.append(150000)
                elif ukuran[i] == "40" :
                    harga.append(150000)
                elif ukuran[i] == "41" :
                    harga.append(150000)
                else :
                    print("Ukuran tidak tersedia")
                    harga.append(0)
            else :
                print("eror karena salah input")
                exit()
    proses()

    # proses perhitungan
    def hitung() :
        global ubay
        global jumbay
        jumbay = 0
        for i in range(banyakjenis) :
            jmlhharga.append(harga[i]*jmlhpotong[i])
            jumbay = jumbay+jmlhharga[i]
        print("")
        print("Proses Perhitungan...")
        print("Total\t\t   : Rp.","{:,}".format(jumbay))
        ubay = int(input("Masukan uang bayar : Rp. "))
        if ubay > jumbay :
            print("Kembalian\t   : Rp.","{:,}".format(ubay-jumbay))
        elif ubay == jumbay :
            print("Kembalian\t   : Rp. 0")
        else :
            print("Kurang\t\t   : Rp.","{:,}".format(ubay-jumbay))
        print("")
    hitung()

    #output
    def struk() :
        print("Proses mencetak struk...")
        print("--------------------------------------------------")
        print("\t\tJ-Da\'an clothes")
        print("\t Jl. Raya Halim kusuma no. 18")
        print("\t     Telp/wa 085877624931")
        print("--------------------------------------------------")
        print("\t     ",tgl_jam)
        print("--------------------------------------------------")
        tblStruk = {
        "Merk": merk,
        "Ukuran": ukuran,
        "Qty": jmlhpotong,
        "Harga": harga,
        "Total": jmlhharga,
        }
        strukPandas = pd.DataFrame(tblStruk)
        print(strukPandas)
        print("") 
        print("--------------------------------------------------")
        print("\t\t\tTotal\t  : Rp.","{:,}".format(jumbay))
        print("\t\t\tBayar\t  : Rp.","{:,}".format(ubay))
        if ubay > jumbay :
            print("\t\t\tKembalian : Rp.","{:,}".format(ubay-jumbay))
        elif ubay == jumbay :
            print("\t\t\tKembalian : Rp. 0")
        else :
            print("\t\t\tKurang    : Rp.","{:,}".format(ubay-jumbay))
        print("--------------------------------------------------")
        print("\t\tTERIMAKASIH")
        print("\t   SELAMAT BELANJA KEMBALI")
    struk()