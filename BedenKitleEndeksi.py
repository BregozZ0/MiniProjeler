# Beden kitle endeksi = Kilo / boy*boy
# 25'ten büyükse obez
# 18-25 arasındaysa normal
# 18'ten küçükse zayıf

kilo = int(input("Kilonuzu giriniz : "))
boy = float(input("Boyunuzu giriniz : "))

bke = kilo / (boy*boy)

if bke < 25 and bke > 18:
    print("Normalsiniz")
elif bke < 18:
    print("Zayıfsınız")
elif bke > 25:
    print("Obezsiniz")
