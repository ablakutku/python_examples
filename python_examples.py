# ODEV 1
# === ÖDEV kullanıcıdan girilen 2 veri alıyruz eğer sayılardan oluşuyorsa ikisini
# toplasın değilse ekrana "yalnızca sayı girilsin"

#--------------------------------------------------------------------------------------------------------------------------------------------------#

sayi1 = input("Birinci sayıyı giriniz: ")
sayi2 = input("İkinci sayıyı giriniz: ")

if sayi1.isnumeric() and sayi2.isnumeric():
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
    print(sayi1 + sayi2)
else:
    print("Lütfen sayı giriniz")
#ODEV 2
# ===== ÖDEV =====
# vize ve final iki not inputtan alınır
# vizenin ortalaması %40 finalin ortalaması %60tır.
# iki notun ortalaması alınıp çıkan sonuç
# 100 90 arası "AA"- 90 80 arası "AB" - 80 70 arası "BB"- 70 60 arası "CB" - 60 50 "CC"
# ekrana yazdır

#--------------------------------------------------------------------------------------------------------------------------------------------------#

# vize = int(input("Vize notunuzu giriniz : "))
# final = int(input("Final notunuzu giriniz : "))
# ortalama = (vize*0.4)+(final*0.6)
# print("Ortalamanız : ",ortalama)
# if ortalama >= 90:
#     print("AA")
# elif ortalama >= 70:
#     print("BB")
# elif ortalama >= 60:
#     print("CB")
# elif ortalama >= 50:
#     print("CC")


#ODEV 3
# ===== ÖDEV =====
# Kullanıcıya sinema ya da tiyatro tercihi sorulsun.
# sinema 20tl tiyatro 10tl öğrenciyse %50 indirim yapılacak

#--------------------------------------------------------------------------------------------------------------------------------------------------#

# secim = str(input("Hangi alana gireceksiniz? Tiyatro veya Sinema: "))
# calisma = str(input("Çalışıyor musunuz? Evet veya Hayır: "))
# ogrenci = str(input("Öğrenci misiniz? Evet veya Hayır: "))

# sinema = 20
# tiyatro = 15

# if ogrenci == "Evet":
#     sinema = sinema - (sinema*0.5)
#     tiyatro = tiyatro - (tiyatro*0.5)
#     if calisma == "Evet":
#         sinema = sinema - (sinema*0.1)
#         tiyatro = tiyatro - (tiyatro*0.1)
#         if secim == "Sinema":
#             print("Sinema bilet fiyatınız : ",sinema)
#         elif secim == "Tiyatro":
#             print("Tiyatro bilet fiyatınız : ",tiyatro)
#     elif calisma == "Hayır":
#         if secim == "Sinema":
#             print("Sinema bilet fiyatınız : ",sinema)
#         elif secim == "Tiyatro":
#             print("Tiyatro bilet fiyatınız : ",tiyatro)
