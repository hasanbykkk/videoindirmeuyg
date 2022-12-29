from pytube import YouTube
import datetime
def bilgilerigöster():

    url=YouTube(input("bigilerini göreceğiniz videonun linki"))
    sondk=url.lenght/60
    print("videonun başlığı",url.title)
    print("videonun sahibi",url.author)
    print("videonun küçük resmi",url.thumbnail_url)
    print("videonun izlenmesi",url.views)
    print("videonun uzunluğu",sondk,"dakika")

def videoindir():
      url=YouTube(input("bigilerini göreceğiniz videonun linki"))
      indirmebağlantı=url.stream.filter(progressive="True").first()
      indirmebağlantı.Download()
      print("indirilen video bilgileri")
      print("videonun başlığı",url.title)
      print("videonun sahibi",url.author)
      print("videonun küçük resmi",url.thumbnail_url)
      print("videonun izlenmesi",url.views)
      print("videonun uzunluğu",sondk,"dakika")
def sesindir():
     url=YouTube(input("bigilerini göreceğiniz videonun linki"))
     indirmebağlantı=url.stream.filter(mime_type="audio/mp4").first()
     indirmebağlantı.Download()
     print("indirilen video bilgileri")
     print("videonun başlığı",url.title)
     print("videonun sahibi",url.author)
     print("videonun küçük resmi",url.thumbnail_url)
     print("videonun izlenmesi",url.views)
     print("videonun uzunluğu",sondk,"dakika")

while True:

    seç=input("1-bilgileri gösterme\n2-video indirme\n3-ses indirme")
    if seç=="1":
         bilgilerigöster()

    elif seç=="2":
          videoindir()

    elif seç=="3":
        sessesindir()
    else:
        print("çıkış yapılıyor")
        time.sleep(1)
        print("5")
        time.sleep(1)
        print("4")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        print("çıkış yapıldı...")




      

