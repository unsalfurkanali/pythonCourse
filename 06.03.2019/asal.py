def asal(x):                    #Sayının asallığını bulan fonksiyon. x asal ise True, değilse False çevirir
    for i in range(2, x, 1):    #i 2->x arasında 1'er artarak;
        if x % i == 0:          #x'in i'ye bölümünden kalan sıfır mı?
            return False        #False çevir
    return True                 #Döngüden çıktıysa tam böleni yoktur. True çevir

print(asal(8))