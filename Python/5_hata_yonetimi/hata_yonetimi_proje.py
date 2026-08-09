notlar = []
hata_sayisi = 0

with open("notlar.txt", "r", encoding = "utf-8") as dosya:
    for satir in dosya:
        try:
            not_deger = int(satir.strip())
            notlar.append(not_deger)
        except ValueError:
            print(f"Hatalı veri bulundu {satir.strip()}")
            hata_sayisi += 1

print(f"Notlar: {notlar}")
print(f"Hata sayısı: {hata_sayisi}")

ortalama = sum(notlar)/len(notlar)

print(f"Ortalama: {ortalama}")