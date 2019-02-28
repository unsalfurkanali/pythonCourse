i, toplam = 0, 0            #Döngü sayacı ve sayıların toplamını tutacak değişkenlere başlangıç değeri atanıyor
while i < 10:               #i < 10 olduğu sürece aşağıdaki işlemleri tekrarla
    sayi = input("Bir sayı giriniz ")   #Klavyeden sayı okuma
    sayi = int(sayi)                    #Okunan sayının int'e çevrilmesi
    #sayi = int(input("Bir sayı giriniz"))
    toplam = toplam + sayi              #Girilen sayı toplam'a ekleniyor
    i = i + 1                           #Sayaç değişkeni i bir arttırılıyor
ortalama = toplam / 10                  #Ortalama hesaplanıyor
print("Ortalama = {}".format(ortalama)) #Ortalama ekrana yazdırılıyor