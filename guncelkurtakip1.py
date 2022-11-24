from forex_python.converter import CurrencyRates

while True:
    input1 = input("Çevirmek istediğiniz para birimi : ")
    input2 = input("Çevireceğeniz para birimi : ")
    input3 = int(input("Çevirmek istediğiniz parayı giriniz : "))

    fonk = CurrencyRates()
    kur = fonk.get_rate(input2, input1)
    print(f"{input3} {input2} = {input3*float(kur)} {input1}")

    if input1 == input2:
        print("Aynı para birimini çeviremezsiniz!!!")
        break
