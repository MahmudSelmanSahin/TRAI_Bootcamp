#Soru 1
with open("notlar.txt", "w", encoding="utf-8") as dosya:
    dosya.write("50\n")
    dosya.write("60\n")
    dosya.write("45\n")
    dosya.write("90\n")
    dosya.write("82\n")

#Soru 2

notlar = []

with open("notlar.txt", "r", encoding = "utf-8") as dosya:
    for satir in dosya:
        notlar.append(int(satir.strip()))

ortalama = sum(notlar)/len(notlar)
en_yuksek_not = max(notlar)
en_dusuk_not = min(notlar)


#Soru 3

if ortalama > 50:
    sonuc = "Sınıf geçti"
else:
    sonuc = "Sınıf kaldı"

with open("sonuc.txt", "w", encoding = "utf-8") as dosya:
    print(sonuc)