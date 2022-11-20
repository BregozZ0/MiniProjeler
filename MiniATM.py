# MiniATM
# 1-) Güncel bakiyeyi göstersin
# 2-) Para çekme
# 3-) Para yatırma
# 'q' bastığı zaman çıkış yapsın

# Kullanıcıdan yapmak istediği işlem için input alıyoruz.
print(" 1-) Güncel bakiyeyi göstersin\n 2-) Para çekme\n 3-) Para yatırma ")
secim = input("Yapmak istediğiniz işlemi seçiniz : ")
bakiye = 1000

# İşlemleri yazıyoruz.
if secim == "1":
    print("Güncel bakiye ", bakiye)
elif secim == "2":
    cekilecek_tutar = int(input("Çekmek istediğiniz miktarı yazınız : "))
    if cekilecek_tutar <= bakiye:
        print("Güncel bakiyeniz : ", (bakiye-cekilecek_tutar))
    elif bakiye < cekilecek_tutar:
        print("Yetersiz miktar")
elif secim == "3":
    yatirilacak_tutar = int(input("Yatırmak istediğiniz miktarı yazınız : "))
    print("Güncel bakiye : ", (yatirilacak_tutar+bakiye))
elif secim == "q":
    print("ATM uygulamasından çıkış yapılıyor ...")
else:
    print("Lütfen işleminizi seçiniz!!!")
