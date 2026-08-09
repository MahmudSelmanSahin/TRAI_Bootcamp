import numpy as np

#Soru 1
dizi = np.arange(1,21)
print(dizi.size)

#Soru 2
dizi = np.array([5, 10, 15, 20, 25])
carpim = dizi*3
print(carpim)

#Soru3
dizi = np.arange(0,31)
secim = dizi[10:21]
print(secim)

#Soru 4
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

birlesim = np.concatenate((a, b))
print(birlesim)

#Soru 5
dizi = np.arange(1,13)
matris = np.reshape(dizi, (3, 4))
print(matris.shape)

#Soru 6
matris = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(matris[1,:])
print(matris[:,1])

#Soru 7
matris = np.random.rand(3,3)

print(f"Ortalama: ", np.mean(matris))
print(f"Maks: ", np.max(matris))

#Soru 8
a = np.array([2, 4, 6, 8])
b = np.array([1, 3, 5, 7])

eleman_carpim = a * b
print(eleman_carpim)

#Soru 9
dizi = np.arange(1,10)
matris = dizi.reshape(3,3)

print(matris)
print(matris.T)

#Soru 10
dizi = np.random.randint(1,51,10)
toplam = np.sum(dizi)
ortalama = np.mean(dizi)

print(toplam)
print(ortalama)