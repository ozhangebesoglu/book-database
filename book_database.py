import sqlite3 #sqlite3 kütüphanesini ekledik.
import time

db = sqlite3.connect('kitaplık.db') #kutuphaneyi olusturduk.

yetki = db.cursor() #kutuphanede islem ekleyebilmek icin yetkiye cursor ekledik.

print('****VERITABANINA HOSGELDINIZ PROGRAM ACILIYOR LUTFEN BEKLEYINIZ...****')
time.sleep(2)

while True:
    print('----MENU----')
    #kullanicidan secim yapmasini istedik
    secim = input("Yapmak istediginiz islemi seciniz:\n1. Kitap Ekle\n2. Kitapları Listele\n3. Bastan Siralama\n4. Kitap Bul\n5. Programdan Cikis\n")

    if secim == '1':
        kitap_adi = input('Kitap adini girin: ')
        sayfa_sayisi = int(input('Sayfa sayisini girin: '))
        yayin_yili = int(input('Yayin yili girin: '))

        yetki.execute('CREATE TABLE IF NOT EXISTS deneme(Kitabin_Adi,Sayfa_Sayisi,Yayin_Yili)') #Bir tablo yaratip hata almasini onledik ve tabloya verilerimizi ekledik
        yetki.execute(f'INSERT INTO deneme VALUES("{kitap_adi} ", "{sayfa_sayisi}", "{yayin_yili}")') #Tablomuza degerleri ekledik
        
        db.commit() 
        print('Kitap kaydedildi.')
        print('*' * 30)


    elif secim == '2':
            yetki.execute('SELECT * FROM deneme') #Tablodaki verileri cektik
            yazdir = yetki.fetchall()
            sayi = 1
            for i in yazdir:

                print('*** KITAP BILGILERI ***')
                print(f"\n{sayi}: Kitap Adi: {i[0]}\nSayfa Sayisi: {i[1]}\nYayin Yili: {i[2]}\n")
                print('*' * 30)  
                sayi += 1

    elif secim == '3':
        sayfa_sec = int(input('Bastan siralama yapmak istediginiz sayiyi girin: '))#kullanicidan bir sayi degeri alip ve kitap listesini bastan siralayarak yazdirdik
        yetki.execute('SELECT * FROM deneme LIMIT?', (sayfa_sec,))
        yazdir = yetki.fetchall()
        sayi = 1
        for i in yazdir:
            print('*** KITAP BILGILERI ***')
            print(f"\n{sayi}: Kitap Adi: {i[0]}\nSayfa Sayisi: {i[1]}\nYayin Yili: {i[2]}\n")
            print('*' * 30)
            sayi += 1


    elif secim == '4':
        aranacak_kitap = input('Kitap adini girin: ')   #kullanicidan bir kitap adi alip ve kitabin bilgisini yazdirdik
        yetki.execute('SELECT * FROM deneme WHERE Kitabin_Adi LIKE?', ('%' + aranacak_kitap + '%',))
        yazdir = yetki.fetchall()

        if yazdir:
            sayi = 1
            for i in yazdir:
                print('*** KITAP BILGILERI ***')
                print(f"\n{sayi}: Kitap Adi: {i[0]}\nSayfa Sayisi: {i[1]}\nYayin Yili: {i[2]}\n")
                print('*' * 30)
                sayi += 1
        else:
            print('Aradiginiz kitap bulunamadi.')
            print('*' * 30)
        
    
    
    elif secim == '5':
        print('Programdan cikis yapiliyor...')
        db.close()
        time.sleep(2)
        exit()
 
    else:
        print('Yanlis secim yaptiniz. Lutfen tekrar deneyiniz.')
        print('*' * 30)
     


