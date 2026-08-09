import matplotlib.pyplot as plt

""" 
    line plot
"""

gunler = [1, 2, 3, 4, 5]
sicaklik = [22, 24, 23, 25, 27]

plt.plot(gunler, sicaklik, color = "red", linestyle = "--", marker = "o")
plt.title("Günlere göre sıcaklık grafiği")
plt.xlabel("Günler")
plt.ylabel("Sıcaklık")
plt.grid("True")

plt.show()

""" 
    sütun grafikleri
"""

#sütun grafiği oluştur
isimler = ["ali", "ayşe", "mehmet", "zeynep"]
notlar = [70, 85, 60, 90]
renkler = ["red", "blue", "green", "orange"]

plt.bar(isimler, notlar, color = renkler)
plt.title("Öğrenci Notları")
plt.xlabel("Öğrenciler")
plt.ylabel("Notlar")
plt.show()

#yatay sütun grafiği
plt.barh(isimler, notlar)
plt.show()

""" pie chart """

etiketler = ["python", "java", "c++", "javascript"]
degerler = [40, 25, 20, 15]
ayrim = [0, 0.1, 0, 0]
renkler = ["red", "blue", "green", "orange"]

plt.pie(degerler, labels = etiketler, explode = ayrim, autopct = "%1.1f%%", colors = renkler)
plt.title("Proglama dillerinin kullanım oranı")
plt.show()

""" Dağılım Grafiği """

calisma_saatleri = [1, 2, 3, 4, 5, 6]
notlar = [50, 60, 70, 80, 90, 100]

plt.scatter(calisma_saatleri, notlar, color = "green", s=100)
plt.title("Çalışma Saatine Göre Not Dağılım Grafiği")
plt.xlabel("Çalışma Saatleri")
plt.ylabel("Not Durumu")
plt.show()

#birden fazla veri grubu çizdirme

x1 = [1, 2, 3, 4]
y1 = [50, 60, 70, 80]

x2 = [1, 2, 3, 4]
y2 = [55, 65, 75, 85]

plt.scatter(x1, y1, color = "red", s = 50, label = "Diferansiyel")
plt.scatter(x2, y2, color = "green", s = 50, label = "Veri Yapıları")
plt.legend()

plt.show()

""" Birden fazla grafiği aynı anda gösterme (subplots) """

x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [40, 30, 20, 10]

plt.subplot(1, 2 ,1)
plt.plot(x, y1)
plt.title("Grafik 1")

plt.subplot(1,2,2)
plt.plot(x,y2)
plt.title("Grafik 2")

plt.show()

#farklı grafik türleri ile subplot oluşturma

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt. title("Line Plot")

plt.subplot(1, 2, 2)
plt.bar(x, y)
plt.title("bar chart")

plt.show()

# 2x2 grafik oluşturma

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.subplot(2,2,1)
plt.plot(x, y)
plt.title("Grafik 1")

plt.subplot(2,2,2)
plt.bar(x, y)
plt.title("Grafik 2")

plt.subplot(2,2,3)
plt.scatter(x, y)
plt.title("Grafik 3")

plt.subplot(2,2,4)
plt.pie(y)
plt.title("Grafik 4")

plt.show()