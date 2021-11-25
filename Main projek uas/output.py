from datetime import datetime
saat_ini = datetime.now()
tgl_jam = saat_ini.strftime("%d-%m-%Y %H:%M:%S") # format dd/mm/YY H:M:S 

#membuat output struk belanja
def struk() :
    print("\t\tJ-Da\'an clothes")
    print("\tJl. Raya Halim kusuma no. 18")
    print("\t\tTelp/wa 0899999")
    print("----------------------------------------------")
    print("\t     ",tgl_jam)
    print("----------------------------------------------")
    print("Perhitungan barang yang dibeli")
    print("----------------------------------------------")
    print("\t\t\tTotal   : ")
    print("\t\t\tBayar   : ")
    print("\t\t\tKembali : ")
    print("----------------------------------------------")
    print("\t\tTERIMAKASIH")
    print("\t   SELAMAT BELANJA KEMBALI")

struk()