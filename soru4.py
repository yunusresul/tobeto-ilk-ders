# Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
import math
daireninYariCapi = float(input("Dairenin yarı çapını giriniz. "))
daireninAlani = math.pi * daireninYariCapi*daireninYariCapi
daireninCevresi = math.pi * 2 * daireninYariCapi

sonuc=f"Dairenin Alanı = {daireninAlani} Dairenin Çevresi = {daireninCevresi}"
print(sonuc)
