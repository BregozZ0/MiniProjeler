while True:
	while True:
		try:
			birinci = int(input("Birinci sayıyı giriniz: "))
		except:
			print("Lütfen bir sayı giriniz!!!!!!!!!!!!")
			continue
		else:
			print("OK")
			break

	while True:

		try:
			ikinci = int(input("İkinci sayıyı giriniz: "))
		except:
			print("Lütfen sayı giriniz!!!!!!!!!!!!!!!")
			continue
		else:
			print("OK")
			break

	operator = input("Lütfen işlem seçiniz + , - , * , / :")

	if operator not in "+-*/":
			print("Lütfen sadece +-*/ bunlardan birini giriniz!!!")

	toplam = birinci + ikinci
	cikartma = birinci - ikinci
	carpma = birinci * ikinci
	bolme = birinci / ikinci

	if operator == "+":
		print(f"{birinci} + {ikinci} = {toplam}")
	elif operator == "-":
		print(f"{birinci} - {ikinci} = {cikartma}")
	elif operator == "*":
		print(f"{birinci} * {ikinci} = {carpma}")
	elif operator == "/":
		print(f"{birinci} / {ikinci} = {bolme}")
