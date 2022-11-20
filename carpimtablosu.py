import random

while True:

    # Kolay tablo için değişkenler
    kolay_tablo = random.randint(1, 10)
    kolay_tablo2 = random.randint(1, 10)

    # Orta tablo için değişkenler
    orta_tablo = random.randint(1, 100)
    orta_tablo2 = random.randint(1, 10)

    # Zor table için değişkenler
    zor_tablo = random.randint(1, 100)
    zor_tablo2 = random.randint(1, 100)

    # zorluğu seçmek için değişken
    zorluk_secimi = input("Kolay-Orta-Zor : ")

    # Kolay için if kontrolü
    if zorluk_secimi == "Kolay":

        # soruyu ekrana yazar
        print(f"{kolay_tablo} x {kolay_tablo2} = ?")

        # kullanıcıdan sonucu ister
        kolay_sonuc = int(input("Sonuç : "))

        # doğru cevap için değişken
        kolay_cevap = kolay_tablo * kolay_tablo2

        # son if kontrolü
        if kolay_sonuc == kolay_cevap:
            print("Doğru :)")
        else:
            print(f"Yanlış, doğru cevap {kolay_cevap}")

    if zorluk_secimi == "Orta":

        print(f"{orta_tablo} x {orta_tablo2} = ?")

        orta_sonuc = int(input("Sonuç : "))

        orta_cevap = orta_tablo * orta_tablo2

        if orta_cevap == orta_sonuc:
            print("Doğru :)")
        else:
            print(f"Yanlış, doğru cevap {orta_cevap}")

    if zorluk_secimi == "Zor":

        print(f"{zor_tablo} x {zor_tablo2} = ?")

        zor_sonuc = int(input("Sonuç : "))

        zor_cevap = zor_tablo * zor_tablo2

        if zor_cevap == zor_sonuc:
            print("Doğru :)")
        else:
            print(f"Yanlış, doğru cevap {zor_cevap}")



