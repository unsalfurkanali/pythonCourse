yas = input("Yaşınızı giriniz")         #Kullanıcıdan yaş bilgisini alıp yas değişkenine at
kilo = input("Kilonuzu giriniz")        #Kullanıcıdan kilo bilgisini alıp kilo değişkenine at
boy = input("Boyunuzu giriniz")         #Kullanıcıdan boy bilgisini alıp boy değişkenine at

#str olarak alınan yaş, boy ve kilo bilgileri float* veri tipine çevrilir
yas = float(yas)
kilo = float(kilo)
boy = float(boy)

vki = (kilo)/(boy**2)                   #vki hesaplamak için kullanılan formul

if(yas >= 19 and yas<=24):              #Eğer yaş 19'dan büyük eşit ve 24'ten küçük eşit ise; (koşul1)
    if(vki >= 19 and vki<=24):          #Eğer vki 19'dan büyük eşit ve 24'ten küçük eşit ise;(koşul1a)
        print("İdeal VKİ")              #Ekrana ideal vki yaz
    elif(vki< 19):                      #Eğer koşul1a doğru değil ve vki 19'dan küçük ise; (koşul1b)
        print("Zayıf")                  #Ekrana zayıf yaz
    else:                               #Eğer koşul1a ve koşul1b doğru değilse;
        print("Kilolu")                 #Ekrana kilolu yaz
elif(yas >= 25 and yas<=34):            #Eğer yaş 25'den büyük eşit ve 34'ten küçük eşit ise; (koşul2)
    if(vki >= 20 and vki<=25):          #Eğer vki 20'den büyük eşit ve 25'ten küçük eşit ise;(koşul2a)
        print("İdeal VKİ")              #Ekrana ideal vki yaz
    elif(vki< 25):                      #Eğer koşul1a doğru değil ve vki 19'dan küçük ise; (koşul2b)
        print("Zayıf")                  #Ekrana zayıf yaz
    else:                               #Eğer koşul2a ve koşul2b doğru değilse;
        print("Kilolu")                 #Ekrana kilolu yaz

#*float : Gerçel (Reel) sayıları bellekte tutmak için kullanılan değişkenler float ile belirtilir