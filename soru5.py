# Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
sayi = input("Bir sayı griniz. ")

polindrom = sayi[::-1]

if sayi == polindrom:
    print(sayi , "bir polindrom sayıdır.")
elif sayi != polindrom:
    print(sayi , "bir polindrom sayı değildir")

