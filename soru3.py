#Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
birinciSayi = float(input("Bir sayı giriniz. "))
ikinciSayi = float(input("Bir sayı giriniz. "))
ucuncuSayi = float(input("Bir sayı giriniz. "))

enBuyukSayi = max(birinciSayi,ikinciSayi,ucuncuSayi)
print(f"En büyük sayı = {enBuyukSayi}")