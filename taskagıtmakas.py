import random

while True:

    print("1-) taş")
    print("2-) kağıt")
    print("3-) makas")
    print("Herhangi bir tuşa basıp çıkabilirsiniz")
    secim = input("Seçiminizi yapınız : ")

    bilgisayar = ["taş", "kağıt", "makas", "taş", "kağıt", "makas", "taş", "kağıt", "makas", "taş", "kağıt", "makas"]
    random_secim = random.choice((bilgisayar))

    if random_secim == "makas" and secim == "2":
        print("Yapay zeka kazandı")

    elif random_secim == "taş" and secim == "2":
        print("Siz kazandınız")

    elif random_secim == "kağıt" and secim == "2":
        print("kimse kazanamadı")

    elif random_secim == "makas" and secim == "1":
        print("Siz kazandınız")

    elif random_secim == "kağıt" and secim == "1":
       print("Yapay zeka kazandı")

    elif random_secim == "taş" and secim == "1":
        print("kimse kazanmadı")

    elif random_secim == "makas" and secim == "3":
        print("kimse kazanmadı")

    elif random_secim == "taş" and secim == "3":
        print("Yapay zeka kazandı")

    elif random_secim == "kağıt" and secim == "3":
        print("siz kazandınız")
    else:
        print("Çıkış yapılıyor...")
        break
