print("1-) TRY to DOLAR")
print("2-) DOLAR to TRY")
print("3-) TRY to EURO")
print("4-) EURO to TRY")
print("5-) Çıkış yap")
secim = input("İşlem seçiniz : ")

if secim == "1":
    islem1 = int(input("Çevirmek istediğiniz türk lirası miktarını giriniz : "))
    trytodolar = islem1 / 18.62
    print(trytodolar, " ABD Doları")
elif secim == "2":
    islem2 = int(input("Çevirmek istediğiniz dolar miktarını giriniz : "))
    dolartotry = islem2 * 18.62
    print(dolartotry, " Türk Lirası")
elif secim == "3":
    islem3 = int(input("Çevirmek istediğiniz türk lirası miktarını giriniz : "))
    trytoeuro = islem3 / 19.30
    print(trytoeuro, " Euro")
elif secim == "4":
    islem4 = int(input("Çevirmek istediğiniz euro miktarını giriniz : "))
    eurototry = islem4 * 19.30
    print(eurototry, " Türk Lirası")
elif secim == "5":
    print("Çıkış yapılıyor...")
else:
    print("Lütfen işlem seçiniz")
