import random

print("Sayı tahmin etmeceye hoşgeldiniz :)")
random_sayi = random.randint(1,10)
can = 5

while can > 0:
    tahmin = int(input("Tahmininizi yazınız : "))

    if random_sayi == tahmin:
        print("Doğru bildiniz :) ")
        break
    elif random_sayi != tahmin:
        can -= 1
        print("Yanlış, deneme hakkınız : ", can)

    if can == 0:
        print("Hakkınız biti, doğru cevap : ", random_sayi)
