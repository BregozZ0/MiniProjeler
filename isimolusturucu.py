import random

def isim_olusturucu():
    isim = ["Emin", "Eren", "Muhammed", "Umut", "Batuhan", "Metehan", "Furkan", "Enes", "Burak", "Mehmet"]
    soyisim = ["Uyar", "Çakmak", "Rende", "Çalışkan", "Tutum", "Özdemir", "Aslangül", "Fındık"]
    return "{} {}".format(random.choice(isim), random.choice(soyisim))

for i in range(5):
    print(isim_olusturucu())
