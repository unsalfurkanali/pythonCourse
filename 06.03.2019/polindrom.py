sayac = 0
for i in range(1, 200000, 1):
    s = str(i)
    if s == s[::-1]:        #Sayıyı terse çevirip* kendisi ile karşılaştırıyoruz.
        print("Bir polindrom sayıdır {}".format(s))
        sayac = sayac + 1
print(sayac)

#* Bir str değişkeni içerisindeki ifadeyi(bir sayı da olabilir) ters çevirmek istersek str'nin adı[::-1]
# işlemini kullanmalıyız. Örneğin s = "Python" ise s[::-1] = "nohtyP" olur. Bu işlem sayılarda da geçerlidir
# a = "123" olsun. a[::-1] işleminin sonucu "321" ifadesini verir. Bunun sayı içermekle birlikte sayı(int, float)
# değişeni olmadığına dikkat edin.