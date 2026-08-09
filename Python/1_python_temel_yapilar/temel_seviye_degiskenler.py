""" print(0.1 + 0.2)


fiyat = float(input("Fiyatı giriniz:"))
kdvli_fiyat = fiyat + fiyat*20/100

print("Gerçek fiyat: ", fiyat)
print("KDV'li fiyat: ",kdvli_fiyat)


string_ifade = "Python"

print(string_ifade.replace("o","O"))
print(string_ifade.lower())
print(len(string_ifade))

x = 10
y = "10"
print(type(x)) # type() --> veri tipini gösterir
print(type(y))


sayilar = [1, 2, 3, 4, 5, 6, 7]
sayilar.append(8)
print(sayilar)

sayilar.insert(0, 0) # insert(index, sayi)
print(sayilar)

sayilar.remove(6)
print(sayilar)

sayilar.pop()
print(sayilar)

sayilar.pop(0)
print(sayilar)

sayilar[0] = 777
print(sayilar)


tup = (1, 2, 3) # tuple değiştirilemez
x = (5)  # <class 'int'>
y = (5,) # <class 'tuple'>

#tuple unpacking
koordinat = (10, 20)
x, y = koordinat
print(x)
print(y)

#tuple metotları

n = (7, 7, 20, 30 ,40)
print(n.count(7))
print(n.index(40))
 """
#dictinory(sözlük)

mahmudselmansahin = {
    "İsim": "Mahmud Selman",
    "Soyisim": "Şahin",
    "yas": 20,
    "Şehir": "Antalya",
    "Üniversite": "Konya Teknik Üniversitesi",
    "Bölüm": "Yapay Zeka ve Makine Öğrenmesi",
}

#dictionary'e erişim
""" print(mahmudselmansahin)
print(mahmudselmansahin["yas"])

#dictionary eleman ekleme
mahmudselmansahin["gno"] = 3.41
print(mahmudselmansahin)

#dictionary değer güncelleme
mahmudselmansahin["gno"] = 3.5
print(mahmudselmansahin)

#dictionary eleman silme
del mahmudselmansahin["gno"]
print(mahmudselmansahin)

#anahtarları ve değerleri al

print(mahmudselmansahin.keys())
print(mahmudselmansahin.values())
print(mahmudselmansahin.items()) """


#set (elemanları benzersiz yani unique'dur)

sayilar = {1, 2, 2, 4, 5, 7, 7}
print(sayilar)

#print(sayilar[2]) #hata verir setlerde index yoktur

liste = [1, 2, 3, 4, 5, 6 ,7, 8, 9]
benzersiz = set(liste)
print(benzersiz)

#set'e eleman ekleme
benzersiz.add(0) #eklediğiniz sayinin büyüklüğüne göre yerleştiriyor
print(benzersiz)

#set'den eleman silme
benzersiz.remove(6)
print(benzersiz)

#set işlemleri

a = {2, 1, 3}
b = {5, 3, 4}

print(a.union(b)) #birleştirme yapıyor

print(a.intersection(b)) #kesişim buluyor

