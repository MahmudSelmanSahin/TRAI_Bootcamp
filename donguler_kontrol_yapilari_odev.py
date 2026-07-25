#Soru 1

sayi = int(input("Lütfen bir sayı girin: "))

if sayi > 0:
    print("Pozitif")
elif sayi < 0:
    print("Negatif")
else:
    print("Sıfır")

#Soru 2

i = 1
toplam = 0
for i in range(11):
    print(i)
    toplam += i

print(toplam)

#Soru 3


girdi = ""

while girdi != "q":
    girdi = input("Lütfen mesajınızı giriniz: ")
    print(f"Girdiniz: {girdi}")

print("Çıkış yapıldı")

#Soru 4

for sayi in range(1, 21):
    if sayi > 10:
        boyut = "Büyük"
    else:
        boyut = "Küçük/Eşit"

    if sayi % 2 == 0:
        print(f"{sayi} -> Çift - {boyut}")
    else:
        print(f"{sayi} -> Tek - {boyut}")
    
    