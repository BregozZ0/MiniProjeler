from pytube import YouTube

link = input("Link : ")

print("İndiriliyor...")
YouTube(link).streams.first().download()
print("İndirildi :)")
