# Aylık geliri alıyoruz
from traceback import print_tb


maas = int(input("Gelirinizi yazınız : "))

# Giderleri alıyoruz
gıda_alisveris = int(input("Aylık alişveriş tutarınızı yazınız: "))
kıyafet_alisveris = int(input("Aylık kıyafete harcadığınız tutarınızı yazınız : "))
faturalar = int(input("Faturalarınızın tutarını yazınız : "))
diger = int(input("Bunların haricindeki masraflarınızı yazınız : "))
ev = input("eviniz kira mı (evet/hayır) : ")

if ev == "evet":
    kira_parasi = int(input("Kiranız ne kadar : "))
    toplam_gider = gıda_alisveris + kıyafet_alisveris + faturalar + kira_parasi + diger 
    print(f"Geliriniz {maas}, Toplam gideriniz {toplam_gider}, size kalan {maas-toplam_gider}")
elif ev == "hayır":
    toplam_gider = gıda_alisveris + kıyafet_alisveris + faturalar + diger
    print(f"Geliriniz {maas}, Toplam gideriniz {toplam_gider}, size kalan {maas-toplam_gider}")

kalan = maas - toplam_gider

# Öneriler
if kalan < 500:
    if kıyafet_alisveris > 1000:
        print(f"Kıyafet alışveriş tutarınızı azaltmaya çalışın;{kıyafet_alisveris}")
    
    if faturalar > 1000:
        print(f"Biraz daha tassarruf yapmaya çalışın;{faturalar}")


