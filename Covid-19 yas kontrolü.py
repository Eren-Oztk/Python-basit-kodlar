"""
Covid-19 Yaş kontrolü
20.12.2020
Eren Özatak
"""

print("""
            COVİD -19 SALGIN KAPSAMINDA KISITLAMA YAŞ HESAPLAMA HESAPLAMASI
            """)
import time

while True:
 try:
    ad=str(input("1.Adınızı Giriniz:"))
    soyad=str(input("2.Soyadınızı Giriniz:"))
    cinsiyet=str(input("3.Cinsiyyetinizi Belirtiniz(Erkek/Kadın):"))
    yas=int(input("4.Doğum yılınızı giriniz:"))
    print("Lütfen Bekleyiniz...")
    time.sleep(2)
 except ( ValueError,NameError):
    print("Değerlerin Doğruluğunu Kontrol Edin. Tekrar Deneyin")
    continue
 hesapla = (2020 - yas)
 if hesapla<20 :
        print(f"""
      <<<<<<<<<Kişisel Bilgileriniz>>>>>>>>> 
       |__________________________________|            
       |   Adı:{ad}          
       |   Soyadı:{soyad}        
       |   Cinsiyet:{cinsiyet}      
       |   Yaş:{hesapla}            
       |__________________________________|

    _______________________BİLGİLENDİRME_______________________
    | Küçük Dostumuz Maalesef 20 yaşından küçük olduğun için  |
    | sokağa çıkma kısıtlamasından dolayı çıkamazsın.         |
    |Evinizde kalmanız sizin için daha iyi olacaktır.         |
    _____________________________________________________________""")

 elif hesapla >64:
        print(f"""
      <<<<<<<<<Kişisel Bilgileriniz>>>>>>>>> 
       |__________________________________|            
       |   Adı:{ad}          
       |   Soyadı:{soyad}        
       |   Cinsiyet:{cinsiyet}      
       |   Yaş:{hesapla}            
       |__________________________________|

________________________________BİLGİLENDİRME_________________________________________
|   Değerli Büyüğümüz maalesef sokağa çıkma kısıtlamanız bulunduğu için çıkamazsınız.|
|   Evinizde kalmanız sizin için daha iyi olacaktır...                               |
______________________________________________________________________________________""")
 else:
       print(f"""
      <<<<<<<<<Kişisel Bilgileriniz>>>>>>>>> 
       |__________________________________|            
       |   Adı:{ad}          
       |   Soyadı:{soyad}        
       |   Cinsiyet:{cinsiyet}      
       |   Yaş:{hesapla}            
       |__________________________________|

___________________________________BİLGİLENDİRME______________________________________
|     Tedbirler kapsamında hafta içi saat sabah 05.00 ve akşam 21:00 arası sokağa çıkabilirsiniz.
                            Unutmayın MASKE-MESAFE-TEMİZLİK!   |
|____________________________________________________________________________________|""")








