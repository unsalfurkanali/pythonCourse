def asal(x):            #Asallığı bulan fonksiyon
    for i in range(2, x-1, 1):
        kalan = x % i
        if kalan == 0:
            return False
    return True

def chenIkıAsalinCarpimi(y):    #y sayısının iki asalın çarpımı olma durumunu bulan fonksiyon
    for k in range(2, y-4, 1):  #k : 2->y-4'e kadar
        if y % k == 0:          #Eğer y, k'ya tam bölünüyor ise
            if asal(k):         #k sayısı asal mı?
                if asal(y/k):   #y/k asal mı?*
                    print("Asal çarpanlar = {}, {}  ".format(k, y/k))
                    return True #Asal ise True çevir
    return False                #Eğer for döngüsünden çıktıysa False çevir
#* Eğer bir x sayısı'nın iki asalın çarpımı olma durumunu inceleyeceksek; öncelikle bu sayıyı tam bölen
# en küçük asal sayıyı bulmamız gerekir. Ardından x'i bulunan sayıya böldüğümüzde elde edilen bölümde asal
# sayı ise x sayısı iki asalın çarpımı şeklinde yazılabilir.
# Örneğin x % k = 0 eşitliğini sağlayacak bir k sayısı bulundu. k sayısı asal ise bu sefer x/k sayısının
# asallığı araştırılır. Eğer x/k'da asal ise x iki asalın çarpımı şeklinde yazılabilir; x = k*(x/k)



toplam = 0

for j in range(2, 100, 1):
    if asal(j):
        if asal(j+2):
            toplam = toplam + 1
            print("Direk : {}\n".format(j))
        elif chenIkıAsalinCarpimi(j+2):
            toplam = toplam + 1
            print("Bölümünden : {}\n".format(j))

print(toplam)