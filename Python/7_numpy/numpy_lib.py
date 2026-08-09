import numpy as np

""" sayilar = [1, 2, 3, 4, 5, 6]
print(sayilar)

dizi = np.array(sayilar)
print(dizi)

print(type(dizi))

print(dizi.shape)

print(dizi.dtype)

dizi = np.zeros(5)
print(dizi)

dizi = np.arange(0, 10)
print(dizi)

dizi = np.arange(0, 10, 2)
print(dizi)

dizi = np.linspace(0, 10, 5)
print(dizi)

a = np.array([1, 2, 3, 4])
print(np.sum(a))

print(np.mean(a))

print(np.max(a))
print(np.min(a))

print(np.std(a))
 """
#dizilerde indeksleme

dizi = np.array([10,20, 30, 40, 50])
print(dizi[0])

print(dizi[-1])

print(dizi[1:4])

print(dizi[::2])

matris = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
print(matris)

print(matris[0, 2])
print(matris[1, :])
print(matris[:, 0])
print(matris[:2, :2])

#dizi birleştirme

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

sonuc = np.concatenate((a, b))
print(sonuc)

a = np.array(
    [
        [1, 2],
        [3, 4]
    ]
)

b = np.array(
    [
        [5, 6],
        [7, 8]
    ]
)

sonuc = np.concatenate((a, b))
print(sonuc)

# axis = 0 -> satır yönünde birleştirme
# axis = 1 -> sütun yönünde birleştirme

sonuc = np.concatenate((a,b), axis = 1)
print(sonuc)

#vstack -> dikey yönde birleştirme

sonuc = np.vstack((a, b))
print(sonuc)

#hstack -> yatay birleştirme

sonuc = np.hstack((a, b))
print(sonuc)

#diziyi parçalara bölme

dizi = np.array([1, 2, 3, 4, 5, 6])

sonuc = np.split(dizi, 3)
print(sonuc)

matris = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
)

sonuc = np.split(matris, 2)
print(sonuc)

sonuc = np.split(matris, 3, axis = 1)
print(sonuc)

#çok boyutlu diziler

print(matris.shape)
print(matris.ndim)
print(matris.size)

dizi3 = np.array(
    [
        [
            [1, 2],
            [3, 4]
        ],
        [
            [5, 6],
            [7, 8]
        ]
    ]
)

print(dizi3)
print(dizi3.shape)

dizi = np.arange(12)
print(dizi)

#matrise dönüştürme

matris = dizi.reshape(3,4)
print(matris)

a = np.array(
    [
        [1, 2],
        [3, 4]
    ]
)

b = np.array(
    [
        [5, 6],
        [7, 8]
    ]
)

print(a)
print(b)

print(a + b) # 4 işlem oluyor eleman bazlı

#matris çarpımı

sonuc = np.dot(a, b)
print(sonuc)

print(a.T)

det = np.linalg.det(a)
print(det)

ters = np.linalg.inv(a)
print(ters)

#rastgele ondalık sayı üretme [0-1] arasında
rastgele = np.random.rand(5)
print(rastgele)

#rastgele matris oluşturma
rastgele = np.random.rand(3, 3)
print(rastgele)

#rastgele tam sayı üretme
rastgele = np.random.randint(1, 10, 5)
print(rastgele)

#rastgele tam sayı matrisi üretme

rastgele = np.random.randint(1, 20, (3, 4))
print(rastgele)

#aynı rastgele sonuç
np.random.seed(42)
rastgele = np.random.rand(5)
print(rastgele)

#diziden rastgele eleman seçmek
dizi = np.array([10, 20 ,30, 40, 50])
secim = np.random.choice(dizi)
print(secim)

#diziden birden fazla rastgele eleman seçmek
dizi = np.array([10, 20 ,30, 40, 50])
secim = np.random.choice(dizi, 3)
print(secim)