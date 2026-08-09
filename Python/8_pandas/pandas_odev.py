import pandas as pd

veri = {
    "isim": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Ahmet", "Elif"],
    "yas": [25, 30, 28, 35, 22, 27],
    "sehir": ["Ankara", "İstanbul", "Ankara", "İzmir", "Bursa", "İstanbul"],
    "maas": [5000, 7000, 6000, 8000, 4500, 6500]
}

df = pd.DataFrame(veri)
print("VERİ SETİ")
print(df)
print("\n")

#Soru 1
print("SORU 1 - CEVAP")
print(df.head(3))
print("\n")

#Soru 2
print("SORU 2 - CEVAP")
print(df.columns)
print("\n")

#Soru 3
print("SORU 3 - CEVAP")
print(df["isim"])
print("\n")

#Soru 4
print("SORU 4 - CEVAP")
print([["isim", "maas"]])
print("\n")

#Soru 5
print("SORU 5 - CEVAP")
print(df[df["yas"] > 28])
print("\n")

#Soru 6
print("SORU 6 - CEVAP")
print(df[df["maas"] > 6000][["isim", "maas"]])
print("\n")

#Soru 7
print("SORU 7 - CEVAP")
print(df.sort_values(["maas"]))
print("\n")

#Soru 8
print("SORU 8 - CEVAP")
print(df.sort_values(["maas"], ascending = False))
print("\n")

#Soru 9
print("SORU 9 - CEVAP")
print(df.groupby("sehir")["maas"].mean())
print("\n")

#Soru 10
print("SORU 10 - CEVAP")
df["yillik_maas"] = 12 * df["maas"]
print(df)