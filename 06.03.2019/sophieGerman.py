def asal(x):                #Asallığı bulan fonksiyon
    for i in range(2, x, 1):
        if x % i == 0:
            return False
    return True

sayi = 0

for p in range(2, 100, 1):          # p : 2->100 arasında
    if asal(p) and asal(2*p+1):     #Eğer p asal ve 2p+1 'de asal ise
        sayi = sayi + 1             #Sayacı bir arttır
        print("{} ve {}".format(p, 2*p+1))  #Sophie Asallarını Ekrana Yazır

print("100,000'e kadar olan Sophie German = {}".format(sayi))