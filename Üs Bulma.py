"""
Üs Bulma Hesaplama Programı
Eren Özatak
29.11.2020
"""
import time

print(""" \n\n\t\t\t\t-*-*-*-*-*-*-*\Üs Hesaplama Programı/*-*-*-*-*-*-*""")
print("""               *                                                 *\n\t\t\t   *\t\t\t\t  Yapılabilen Işlemler.          *
               *\t\t\t*-----------------------*            *
               *\t-/-\t-/-\t|1>. Kat Sıfır          | -/- -/-\t *             
               *\t-/-\t-/-\t|2>. Kat İki            | -/- -/-\t *            
               *\t-/-\t-/-\t|3>. Kat Üç             | -/- -/-\t *             
               *\t-/-\t-/-\t|4>. Kat Dört           | -/- -/-\t *            
               *\t-/-\t-/-\t|5>. Kat Beş            | -/- -/-\t *            
               *\t-/-\t-/-\t|6>. Kat Altı           | -/- -/-\t *             
               *\t-/-\t-/-\t|7>. Kat Yedi           | -/- -/-\t *            
               *\t-/-\t-/-\t|Çikiş İçin "8" Basiniz.| -/- -/-\t *            
               *\t\t\t*-----------------------*            *
               *                                                 *
               *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
""")
while True:
 try:
     secim=int(input("""______________________________________________________________
|Yapılacak İşlem Secenegi:\n>>"""))
     time.sleep(0.2)
     if secim == 8:
      print("""____________________________
    Çıkış Yapılıyor...
____________________________""")
      time.sleep(0.5)
      print("""Çıkış Yapıldı.
""")
      break

 except (NameError, ValueError):
    print(">>>>>>>Sadece Belirlenen Değerler(1,2,3,4,5,6,7,8)...");
    continue
 try:
     sayi = int(input("""______________________________________________________________
|Hesaplanılacak sayıyı giriniz:\n>>"""))
 except (NameError,ValueError):
     print(">>>>>>> Hesaplama İçin Sadece Rakam Girilebilir!");
     continue
 if secim==1:
     if sayi==0:
        print("~~~~0 üssü 0 Belirsizdir...~~~~")
        continue
     s=sayi**0
     time.sleep(0.5)
     print(f"---------------->  {sayi} Üssü 0'dan Sonuç=", s,"<----------------")
 elif secim==2:
     h=sayi**2
     time.sleep(0.5)
     print(f"---------------->  {sayi} Üssü 2'den Sonuç=", h,"<----------------")
 elif secim==3:
     r=sayi**3
     time.sleep(0.5)
     print(f"---------------->  {sayi} Üssü 3'ten Sonuç=", r,"<----------------")
 elif secim==4:
     o=sayi**4
     time.sleep(0.5)
     print(f"---------------->  {sayi} Üssü 4'ten Sonuç=", o,"<----------------")
 elif secim==5:
     z=sayi**5
     time.sleep(0.5)
     print(f"---------------->  {sayi} Üssü 5'ten Sonuç=", z,"<----------------")
 elif secim==6:
     t=sayi**6
     time.sleep(0.5)
     print(f"---------------->  {sayi} Üssü 6'dan Sonuç=", t,"<----------------")
 elif secim==7:
     k=sayi**7
     time.sleep(0.5)
     print(f"----------------> {sayi} Üssü 7'den Sonuç=", k,"<----------------")
 else:
     time.sleep(0.5)
     print(">>>>>>>Tanımlı değerleri giriniz!(1,2,3,4,5,6,7,8)")









