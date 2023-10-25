# Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
eskiMaas = float(input("Maaşınızı giriniz. "))
zamOrani = float(input("Zam oranını giriniz. "))

yeniMaas = ((eskiMaas * zamOrani)/100)+eskiMaas
print(f"Zamlı maaşınız: {yeniMaas}" )