print("""
************************************************
Geometrik Şekil Hesaplama Programına Hoşgeldiniz

İlk Olarak İşlem Yapmak İstediğiniz Geometrik Şekli Seçiniz:

Üçgen için 1'i

Dörtgen İçin 2'yi Seçiniz.
************************************************
""")

şekil = input("Lütfen İstediğiniz Geometrik Şekli Seçiniz:")

if şekil == "1":
    print("Üçgeni seçtiniz. Lütfen şeklin 3 kenarının uzunluklarını sırayla giriniz")
    a = int(input("1.kenar:"))
    b = int(input("2.kenar:"))
    c = int(input("3.kenar:"))
    if (abs(b-c) < a < b+c and abs(a-c) < b < a+c and abs(a-b) < c < a+b):
        if a == b == c:
            print("Üçgeniniz bir eşkenar üçgendir.")
        elif (a == b and a != c) or (b == c and b != a) or(a == c and b != c):
            print("Üçgeniniz İkizkenar üçgendir.")
        else:
            print("Sıradan bir üçgendir.")
    else:
        print("Bir üçgen belirtmiyor....")
elif şekil == "2":
    print("Dörtgeni seçtiniz. Lütfen şeklin 4 kenarının uzunluklarını sırayla giriniz")
    a = int(input("1.kenar:"))
    b = int(input("2.kenar:"))
    c = int(input("3.kenar:"))
    d = int(input("4.kenar:"))
    if a == b and a == c and a == d:
        print("Dörtgeniniz bir kare")
    elif a == c and b == d:
        print("Dörtgenininz bir dikdörtgen")
    else:
        print("Sıradan bir dörtgen")
else:
    print("Lütfen Geçerli Bir Değer Giriniz...")