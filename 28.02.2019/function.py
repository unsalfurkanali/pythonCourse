#Bir fonksiyon tanımlamak için;
#def FONKSİYONADI(EĞER VARSA GİRİŞ PARAMETRE İSİMLERİ):
    #FONSİYON İÇERİĞİ
    #GEREKLİ İSE;
    #return GERİ ÇEVRİLECEK PARAMETRE

def menu():              #Herhangi bir parametre almayan menu yazdırma fonksiyonu
    print("1-Toplama")
    print("2-Çıkarma")
    print("3-Çarpma")
def toplama(x, y, z):    #Parametre olarak girilen 3 sayının toplamını geri çeviren fonksiyon. fonksiyonu toplama(1,2,3) şeklinde çağırırsak 6 geri gönderir
    top = x + y + z
    return top           #top değişkeni geri gönderiliyor

menu()
print(toplama(1,2,8))
toplam = toplama(8, 75, 45)
toplam = toplam * 3
print(toplam)
