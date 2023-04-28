import colorama
from colorama import Fore
import os
import time

global sifre
sifre = input(Fore.RED+"Şifre Giriniz\n-->")

def tekrar():
    tekrarislem = input(Fore.YELLOW+"Tekrar işlem yapmak ister misiniz?\n-->")
    if tekrarislem.upper() == "H":
        read = ""
        for i in "Görüşmek üzere...        ":
            read = read+i
            print(Fore.YELLOW+read)
            time.sleep(0.05)
            os.system("cls")
    elif tekrarislem.upper() == "E":
        program()
    else:
        print(Fore.RED+"Lütfen Doğru işlem giriniz!")
        time.sleep(1)
        os.system("cls")
        program()

def program():
    if sifre == "123456":

        global sifre_dogru
        text = ""
        for i in "Ön Muhasebe programına Hoşgeldiniz!              ":
            text = text + i
            print(text)
            time.sleep(0.05)
            os.system("cls")

        # Gelir ve gider listeleri
        gelirler = []
        giderler = []

        # Menü seçeneklerini göster
        while sifre:
            print(Fore.YELLOW+"\nLütfen bir işlem seçin:\n1)Gelir Gir\n2)Gider Gir\n3)Bilanço Göster\n4)Çıkış")
            
            secim = input(Fore.CYAN+"Seçiminizi yapın (1-4): ")

            if secim == "1":
                try:
                    global gelir_miktari
                    gelir_miktari = float(input(Fore.GREEN+"Gelir miktarını girin\n-->"))
                    gelirler.append(gelir_miktari)
                    print(Fore.GREEN+"Gelir kaydedildi.")
                    time.sleep(0.5)
                    os.system("cls")
                except ValueError:
                    print(Fore.RED+"Lütfen sayı giriniz.")
                    gelir_miktari = float(input(Fore.GREEN+"Gelir miktarını girin\n-->"))
            elif secim == "2":
                try:
                    gider_miktari = float(input(Fore.GREEN+"Gider miktarını girin\n-->"))
                    giderler.append(gider_miktari)
                    print(Fore.GREEN+"Gider kaydedildi.")
                    time.sleep(0.5)
                    os.system("cls")
                except ValueError:
                    print(Fore.RED+"Lütfen sayı giriniz.")
                    time.sleep(1)
                    os.system("cls")
            elif secim == "3":
                # KDV'siz toplam gelir ve gider hesaplaması
                toplam_gelir = sum(gelirler)
                toplam_gider = sum(giderler)

                # KDV tutarı hesaplaması
                kdv_tutari = (toplam_gelir - toplam_gider) * 0.18

                # KDV'li toplam gelir ve gider hesaplaması
                toplam_gelir_kdvli = toplam_gelir + kdv_tutari
                toplam_gider_kdvli = toplam_gider + kdv_tutari

                # Bilanço tablosunu göster
                os.system("cls")
                print(Fore.GREEN+"\n----------Bilanço---------")
                print("{:<15s}{:<15s}{:<15s}".format(Fore.GREEN+"Kalem", "KDV'siz Miktar", "KDV'li Miktar"))
                print("-" * 45)
                print("{:<15s}{:<15.2f}{:<15.2f}".format(Fore.GREEN+"Gelirler", toplam_gelir, toplam_gelir_kdvli))
                print("{:<15s}{:<15.2f}{:<15.2f}".format(Fore.GREEN+"Giderler", toplam_gider, toplam_gider_kdvli))
                print("{:<15s}{:<15.2f}{:<15.2f}".format(Fore.GREEN+"Bilanço", toplam_gelir - toplam_gider, toplam_gelir_kdvli - toplam_gider_kdvli))
            elif secim == "4":
                read = ""
                for i in "Görüşmek üzere...        ":
                    read = read+i
                    print(Fore.YELLOW+read)
                    time.sleep(0.05)
                    os.system("cls")

                break
            else:
                print(Fore.RED+"Hatalı seçim. Lütfen tekrar deneyin")

if sifre == "123456":
    program()
else:
    sifre = input(Fore.RED+"Yanlış şifre(Son hak)\nŞifre Giriniz\n-->")
    if sifre == "123456":
        program()
    else:
        print(Fore.RED+"Program Sonlandırılıyor")