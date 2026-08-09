""" İnit metodu """

class Ogrenci:
    def __init__(self, isim, yas):
        print(f"Yeni bir öğrenci oluşturuluyor: isim: {isim}, yas: {yas}")

#nesne oluşturma
ogrenci1= Ogrenci("Ali", 21)

""" attribute """

class Ogrenci:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

#attribute kullanımı
ogrenci1 = Ogrenci("Ali", 21)

#ogrenci1 nesnesinin attributelarına nasıl ulaşabiliriz
print(ogrenci1.isim)
print(ogrenci1.yas)

""" Metot """

class Ogrenci:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def tanit(self):
        print(f"Merhaba benim adım {self.isim}")

ogrenci1 = Ogrenci("Ali", 21)

ogrenci2 = Ogrenci("Kaan", 25)

ogrenci1.tanit()
ogrenci2.tanit()

""" Object oluşturma ve class kullanımı """

class Kitap:

    def __init__(self, ad, yazar, sayfa):
        self.ad = ad
        self.yazar = yazar
        self.sayfa = sayfa

    def bilgi_goster(self):
        print(f"Kitap: {self.ad}")
        print(f"Yazar: {self.yazar}")
        print(f"Sayfa Sayısı: {self.sayfa}")


kitap1 = Kitap("Python Programlama", "Kaan", 500)

#attribute'e erişim
print(kitap1.ad)
print(kitap1.yazar)
print(kitap1.sayfa)

#metot
kitap1.bilgi_goster()

#birden fazla obje oluşturma

kitap1 = Kitap("Python Programlama", "Kaan", 500)
kitap2 = Kitap("Python Programlamaya Giriş", "Can", 150)
kitap3 = Kitap("Python", "Selman", 250)

print(kitap2.ad)
kitap3.bilgi_goster()