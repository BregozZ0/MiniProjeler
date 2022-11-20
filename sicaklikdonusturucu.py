print(" 1-) Selsius to kelvin \n 2-) Kelvin to selsius")
secim = input("Yapmak istediğiniz işlemi seçiniz : ")

if secim == "1":
    sicaklik = int(input("Sıcaklık değerinizi giriniz : "))
    sicaklik += 273
    print(sicaklik, " kelvin")
elif secim == "2":
    sicaklik = int(input("Sıcaklık değerinizi giriniz : "))
    sicaklik -= 273
    print(sicaklik, " Selsius")
else:
    print("Lütfen işleminizi seçiniz!!!")
