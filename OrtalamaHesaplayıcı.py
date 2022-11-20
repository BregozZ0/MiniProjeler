# Öğrenciden 3 notunu al
# 100-85 arası takdir
# 85-70 arası teşekkür
# 50-70 arası boş
# 50 nin altı kalıyor

not1 = int(input("Birinci sınav notunuzu giriniz : "))
not2 = int(input("İkinci sınav notunuzu giriniz : "))
not3 = int(input("Üçüncü sınav notunuzu giriniz : "))

ortalama = (not1 + not2 + not3) / 3

if ortalama <= 100 and ortalama >= 85:
    print("Takdir name")
elif ortalama < 85 and ortalama >= 70:
    print("Teşekkür name")
elif ortalama < 70 and ortalama >= 50:
    print("Boş")
elif ortalama < 50:
    print("Kaldı")
