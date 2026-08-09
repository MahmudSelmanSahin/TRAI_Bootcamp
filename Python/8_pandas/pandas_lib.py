import pandas as pd

veri = pd.Series([10, 20, 30, 40, 50])
print(veri)

veri = pd.Series([10, 20, 30, 40, 50])
print(veri[0])

#Series için özel indeks belirleme
veri = pd.Series([10, 20, 30], index = ["a", "b", "c"])
print(veri)
print(veri["b"])

#Dictionary ile seri oluşturma
veri = {
    "ali": 90,
    "ayşe": 80,
    "nisa": 42
}

s = pd.Series(veri)
print(s)

#series özellikleri
print(s.index)
print(s.values)
print(s.dtype)

#series ile matematiksel işlemler
veri = pd.Series([10, 20, 30 ,40])
sonuc = veri * 2
print(sonuc)

#Series filtreleme
yas = pd.Series([10, 20, 30, 40, 50])
filtre = yas > 25
print(filtre)

sonuc = yas[filtre]
print(sonuc)


#dataframe
veri = {
    "isim":  ["ali", "ayse", "nisa"],
    "yas":   [25, 22, 21],
    "sehir": ["Antalya", "Ankara", "Konya"]
}

df = pd.DataFrame(veri)
print(df)

#sütun isimleri
print(df.columns)

#dataframe satır sayısı öğrenme
print(df.shape)

#sütunlara erişim
print(df["isim"])

#birden fazla sütuna erişim
print(df[["isim", "yas"]])

#yeni sütun ekleme
df["maas"] = [5000, 6000, 7000]
print(df)

#sütun silme
df = df.drop("sehir", axis = 1)
print(df)

#ilk satırları görüntülemek
print(df.head())

#son satırları görüntüleme
print(df.tail())

#dataframe hakkında bilgi alma
print(df.info())

#dosya okuma yazma
df = pd.read_csv("veri.csv")
print(df)

#csv dosyası yazma
veri = {
    "isim": ["selman", "nisa", "hatice"],
    "yas": [20, 21, 57],
    "sehir": ["Antalya", "Konya", "Antalya"]
}

df = pd.DataFrame(veri)

df.to_csv("veri_output_csv", index = False)

#satır seçme : iloc -> slicing tarzı
print(df.iloc[0])

#birden fazla satır seçme 
print(df.iloc[0:3])

#satır seçme : loc -> indeks bazlı seçim yapar
print(df.loc[2])

#belirli bir satır ve belirli bir sütun
print(df.loc[:, ["isim", "yas"]])
print(df.loc[:1, ["isim", "yas"]])

#koşullu filtreleme
filtre =df["yas"] < 25
print(filtre)
sonuc = df[filtre]
print(sonuc)

#birden fazla koşul varsa
sonuc = df[(df["sehir"] == "Konya") & (df["yas"] > 20)]
print(sonuc)

#belirli bir değeri içeren satırlar
sonuc = df[df["sehir"] == "Konya"]
print(sonuc)

#sadece belirli bir sürunu gösterme
print(df[df["yas"] > 20][["isim", "sehir"]])

""" 
    Sütün ve Satır İşlemleri
 """

veri = {
    "isim": ["ali", "ayşe", "mehmet"],
    "yas": [25, 30, 28],
    "maas": [5000, 7000, 6000]
}

df = pd.DataFrame(veri)
print(df)

#yeni bir sütun ekleme
df["sehir"] = ["Ankara", "Konya", "İstanbul"]
print(df)

#hesaplamayla sütun oluşturma
df["yillik_maas"] = 12 * df["maas"]
print(df)

#sütun silme
df = df.drop("maas", axis = 1)
print(df)

#sütun isim değiştirme
df = df.rename(columns={"yillik_maas": "yillikMaas"})
print(df)

#yeni satır ekleme
df.loc[3] = ["Zeynep", 20, "Antalya", 45000 ]
print(df)

#satır silme
df = df.drop(0)
print(df)

#indeks değerlerini yeniden düzenleme
df = df.reset_index(drop = True)
print(df)

""" 
    Veri Sıralama ve Gruplama
"""

veri = {
    "isim": ["ali", "ayşe", "mehmet", "zeynep", "ahmet"],
    "sehir": ["Ankara", "İstanbul", "Ankara", "Antalya", "Antalya"],
    "maas": [5000, 7500, 6000, 9000, 7000]
}

df = pd.DataFrame(veri)
print(df)

#veri sıralama
df_sirali = df.sort_values("maas")
print(df_sirali)

#azalan sıralama
df_sirali = df.sort_values("maas", ascending = False)
print(df_sirali)

#birden fazla sütuna göre sıralama
df_sirali = df.sort_values(["sehir", "maas"])
print(df_sirali)

#veri gruplama: groupby
gruplar = df.groupby("sehir")
print(gruplar)

#grupların ortalama maaşı
sonuc = df.groupby("sehir")["maas"].mean() #şehir bazında ortalama maaş hesaplama
print(sonuc)

#grupların toplam maaşı
sonuc = df.groupby("sehir")["maas"].sum()
print(sonuc)

sonuc = df.groupby("sehir")["isim"].count()
print(sonuc)

#birden fazla işlem yapma
sonuc = df.groupby("sehir")["maas"].agg(["mean", "max", "min"])
print(sonuc)

""" 
    temel pandas fonksiyonları
"""

veri = {
    "isim": ["ali", "ayşe", "mehmet", "zeynep", "ahmet"],
    "yas": [23, 45, 34, 20, 52],
    "sehir": ["Ankara", "İstanbul", "Ankara", "Antalya", "Antalya"],
    "maas": [5000, 7500, 6000, 9000, 7000]
}

df = pd.DataFrame(veri)
print(df)

print(df.head())
print(df.tail(3))
print(df.info())

#sayısal sütunların temel istatistikleri
print(df.describe())

#bir sütundaki değerlerin kaç kez tekrar ettiğini görmek
print(df["sehir"].value_counts())

#bir sütundaki benzersiz değerleri görmek
print(df["sehir"].unique())

#bir sütunda kaç farklı değer olduğunu görmek
print(df["sehir"].nunique())