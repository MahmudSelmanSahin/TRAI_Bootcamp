#Soru 1

ad = "Kaan"
yas = 25
ortalama = 3.45

print(type(ad))
print(type(yas))
print(type(ortalama))

#Soru 2

yas = input("Lütfen yaşınızı giriniz: ")

print(type(yas))

int_yas = int(yas) + 5 
print(int_yas)

#Soru 3

urun_fiyat = float(input("Lütfen ürünün fiyatını giriniz: "))
kdv = urun_fiyat * 18/100
kdvli_urun_fiyat = urun_fiyat + kdv

print(round(kdvli_urun_fiyat,2))

#Soru 4

sayilar = [10, 20 ,30 ,40, 50]

print(sayilar[0])
print(sayilar[-1])
print(sayilar[2:])

sayilar.append(60)
print(sayilar)

sayilar.pop(1)
print(sayilar)

#Soru 5

koordinat = (12, 34)
x, y = koordinat 

""" koordinat[0] = 42 
Traceback (most recent call last):
  File "/Users/mahmudselmansahin/TRAI_Bootcamp/1_python_temel_yapilar/temel_seviye_degiskenler_odev.py", line 47, in <module>
    koordinat[0] = 42
    ~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment """

#Soru 6

ogrenci = {
    "isim": "Ayşe",
    "yas": 22,
    "bolum": "Yazılım"
}

print(ogrenci["isim"])

ogrenci["not"] = 90
ogrenci["yas"] = 23

print(ogrenci)
print(ogrenci.keys())
print(ogrenci.values())

#Soru 7

liste = ["Ali", "Ayşe", "Ali", "Mehmet", " Ayşe"]
benzersiz_isimler = set(liste)

print(benzersiz_isimler)
print(len(benzersiz_isimler))