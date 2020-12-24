print("""
*****Okul Başarı puanı hesaplama*****
""")
isim= input("Öğrencinin adı: ")
soyad=input("Öğrencini soyadı: ")
ders=input("Dersin adı: ")
vize=float(input("Vize notunu giriniz: "))
final=float(input("Final notunu giriniz: "))
ort=(vize * 2/5)+(final* 0.6)
print(isim,soyad,ders,"dersi sınav ortalamanız=",ort)
if ort >10 and ort<=40:
    print("Geçme notunuz(harf ile): FF")
elif ort >45 and ort<50:
    print("Geçme notunuz(harf ile): CC")
elif ort>50 and ort<60:
    print("Geçme notunuz(harf ile): CB")
elif ort>60 and ort<70:
    print("Geçme notunuz(harf ile): BB")
elif ort >70 and ort<85:
    print("Geçme notunuz(harf ile): AB")
elif ort>= 86:
    print("Geçme notunuz(harf ile): AA")
print("Bizi tercih ettiğiniz için teşekkürler.")

