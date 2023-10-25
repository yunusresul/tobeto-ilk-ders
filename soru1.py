#Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
height = float(input("Boyunuuzu m cinsinden giriniz. (Örnek: 1.77 1.88) "))
weight = float(input("Kilonuzu kg cinsinden giriniz. "))

bmi = weight/(height*height)
print("Vücut kitle indeksiniz = " , bmi)

