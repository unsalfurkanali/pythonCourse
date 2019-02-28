sayi = input("Bir sayı giriniz : ")     #Sayı klavyeden okunuyor
sayi = int(sayi)                        #str olarak alınınan sayı int'e çevriliyor
for i in range(2, sayi-1, 1):           #i sayaç değişkeni 1 ile sayı-1 arasında her döngü sonunda 1 artır ve şu işlemleri tekrarla ;
    if sayi % i == 0:                   #Eğer sayı'nın i'ye bölümünden kalan 0'a eşitse
        a = a + 1                       #a'yı bir arttır
#for döngüsü burada bitiyor. Bundan sonra programun normal akışı devam ediyor
if a == 0:                              #Eğer a 0'a eşit ise
    print("Asal")                       #Ekrana asal yaz
else:                                   #Değilse
    print("Asal Değil")                 #Ekrana Asal değil yazdır