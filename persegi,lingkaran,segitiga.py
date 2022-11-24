def persegi_panjang():
    print("menghitung luas persegi panjang")
    panjang = int(input("masukan nilai panjang: "))
    lebar = int(input("masukan nilai lebar: "))
    luas = (panjang*lebar)
    print("luas persegi panjang adalah: ",luas,"cm")

persegi_panjang()

def Lingkaran():
    print("menghitung luas lingkaran")
    phi = float(input("masukan nilai phi: "))
    r = int(input("masukan nilai r: "))
    luas = (phi*r*r)
    print("luas lingkaran adalah: ",luas, "cm")

Lingkaran()

def segitiga():
    print("menghitung luas segitiga")
    alas = int(input("masukan nilai alas: "))
    tinggi = int(input("masukan nilai tinggi: "))
    luas = (alas*tinggi/2)
    print("luas segetiga adalah: ",luas," cm")
    
segitiga()
