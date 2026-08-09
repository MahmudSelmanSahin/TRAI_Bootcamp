class VeriAnalizAraci:
    def __init__(self, veriler):
        self.veriler = veriler

    def verileri_goster(self):
        print(f"Veriler: {self.veriler}")

    def toplam_hesapla(self):
        toplam = sum(self.veriler)
        print(f"Toplam: {toplam}")

    def ortalama_hesapla(self):
        ortalama = sum(self.veriler)/len(self.veriler)
        print(f"Ortalama: {ortalama}")

    def maks_bul(self):
        maks = max(self.veriler)
        print(f"Maksimum: {maks}")

    def min_bul(self):
            minimum = min(self.veriler)
            print(f"Maksimum: {minimum}")

analiz1 = VeriAnalizAraci([10, 20, 30, 40, 50])

analiz1.verileri_goster()
analiz1.toplam_hesapla()
analiz1.ortalama_hesapla()
analiz1.maks_bul()
analiz1.min_bul()