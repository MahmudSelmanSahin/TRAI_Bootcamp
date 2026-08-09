def ortalama_hesapla(vize: float, final: float) -> float:
    ortalama = (vize * 4/10) + (final * 60/100)

    return ortalama

def harf_notu_belirleme(ortalama: float) -> str:
    if ortalama > 82:
        harf_notu = "AA"
    elif ortalama > 72:
        harf_notu = "BA"
    elif ortalama > 65:
        harf_notu = "BB"
    else:
        harf_notu = "FF"

    return harf_notu

def sonuc_yazdir(isim: str, ortalama:float, harf_notu: str):
    print(f"{isim} isimli öğrencinin nihai ortalaması ve harf notu {ortalama},{harf_notu}'dur.")


isim = input("Lütfen öğrencinin ismini giriniz: ")
vize = float(input("Lütfen öğrencinin vize notunu giriniz: "))
final = float(input("Lütfen öğrencinin final notunu giriniz: "))

ortalama = ortalama_hesapla(vize = vize, final = final)
harf_notu = harf_notu_belirleme(ortalama = ortalama)
sonuc = sonuc_yazdir("Mahmud Selman Şahin", ortalama = ortalama, harf_notu = harf_notu)

print(sonuc)