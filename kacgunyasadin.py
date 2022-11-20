import datetime

yil = int(input("Doğudunuz yılı giriniz : "))
ay = int(input("Doğudunuz ayı giriniz : "))
gun = int(input("Doğudunuz günü giriniz : "))

yas = datetime.datetime(yil, ay, gun)
guncel_zaman = datetime.datetime.now()

kac_yildir_yasiyorum = guncel_zaman - yas

print("Kaç gündür yaşıyorsun : ", kac_yildir_yasiyorum.days)
print("Yıl olarak : ", kac_yildir_yasiyorum.days / 365)
