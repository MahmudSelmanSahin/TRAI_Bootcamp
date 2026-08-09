import matplotlib.pyplot as plt

aylar = ["Ocak", "Subat", "Mart", "Nisan", "Mayıs", "Haziran"]
satislar = [120, 150, 170, 160, 200, 220]
karlar = [20, 35, 40, 30, 50, 60]
reklam = [5, 8, 10, 7, 12 ,15]

#Soru 1
plt.plot(aylar, satislar, color = "green")
plt.title("Aylara Göre Satış Durum Grafiği")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")

plt.show()

#Soru 2
plt.plot(aylar, karlar, color = "red")
plt.title("Aylara Göre Kar Grafiği")
plt.xlabel("Aylar")
plt.ylabel("Kâr")

plt.show()

#Soru 3
plt.plot(aylar, satislar, marker = "o")
plt.title("Aylara Göre Satış Durum Grafiği")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")

plt.show()

#Soru 4
plt.bar(aylar, satislar)
plt.title("Aylara Göre Satış Durum Grafiği")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")

plt.show()

#Soru 5
plt.bar(aylar, reklam, color = "green")
plt.title("Aylara Göre Satış Durum Grafiği")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")

plt.show()

#Soru 6
plt.pie(satislar, labels = aylar, autopct = "%1.1f%%")
plt.title("Satışlar Pasta Grafiği")

plt.show()

#Soru 7
plt.scatter(reklam, satislar)
plt.title("Reklam ve Satışlar Dağılım Grafiği")
plt.xlabel("Reklam")
plt.ylabel("Satışlar")

plt.show()

#Soru 8
plt.scatter(reklam, karlar, color = "red", s = 100)
plt.title("Reklam ve Kâr Dağılım Grafiği")
plt.xlabel("Reklam")
plt.ylabel("Kâr")

plt.show()

#Soru 9

plt.subplot(1, 2, 1)
plt.plot(aylar, satislar)
plt.title("Aylara Göre Satış Durum Grafiği")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")

plt.subplot(1, 2, 2)
plt.bar(aylar, karlar)
plt.title("Aylara Göre Kar Grafiği")
plt.xlabel("Aylar")
plt.ylabel("Kâr")

plt.show()

#Soru 10

plt.subplot(2, 2, 1)
plt.plot(aylar, satislar)
plt.title("Aylara Göre Satış Durum Grafiği")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")

plt.subplot(2, 2, 2)
plt.bar(aylar, karlar)
plt.title("Aylara Göre Kar Grafiği")
plt.xlabel("Aylar")
plt.ylabel("Kâr")

plt.subplot(2, 2, 3)
plt.scatter(reklam, satislar)
plt.title("Reklam ve Satışlar Dağılım Grafiği")
plt.xlabel("Reklam")
plt.ylabel("Satışlar")

plt. subplot(2, 2, 4)
plt.pie(satislar, labels = aylar, autopct = "%1.1f%%")
plt.title("Satışlar Pasta Grafiği")

plt.show()
