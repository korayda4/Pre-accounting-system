import colorama
from colorama import Fore ,Style
import os
import time

teksefer = True
global sifre_dogru
sifre_dogru = False
global sifre
sifre = input(Fore.RED+"Şifre Giriniz\n-->")

def tekrar():
    tekrarislem = input(Fore.YELLOW+"Tekrar işlem yapmak ister misiniz?(E/H)\n-->")
    if tekrarislem.upper() == "H":
        read = ""
        for i in "Görüşmek üzere...        ":
            read = read+i
            print(Fore.YELLOW+read)
            time.sleep(0.05)
            os.system("cls")
    elif tekrarislem.upper() == "E":
        os.system("cls")
        program()
        global sifre_dogru
        global teksefer
        sifre_dogru = True
        teksefer = False
    else:
        print(Fore.RED+"Lütfen Doğru işlem giriniz!")
        time.sleep(1)
        os.system("cls")
        program()

def program():
    
        global sifre_dogru
        # Gelir ve gider listeleri
        gelirler = []
        giderler = []
        global teksefer 
        # Menü seçeneklerini göster
        while sifre_dogru:
            if sifre == "123456":
                if teksefer == True:
                    text = ""
                    for i in "Ön Muhasebe programına Hoşgeldiniz!              ":
                        text = text + i
                        print(text)
                        time.sleep(0.05)
                        os.system("cls")
                        teksefer = False
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

                # Vergi payı hesaplaması
                gelir_vergi_payi = toplam_gelir * 0.2
                gider_vergi_payi = toplam_gider * 0.2

                # KDV ve vergi payı toplamları
                kdv_ve_vergi_toplam_gelir = toplam_gelir + kdv_tutari + gelir_vergi_payi
                kdv_ve_vergi_toplam_gider = toplam_gider + gider_vergi_payi

                # Bilanço tablosunu göster
                os.system("cls")


                # Bilanço tablosunu oluştur
                print(Fore.GREEN + Style.BRIGHT + "\n-----------------------------Bilanço-------------------------------------")
                print("|{:<14s}|{:>14s}|{:>14s}|{:>14s}|".format(Fore.GREEN + Style.BRIGHT + "Kalem   ", "KDV'siz Miktar", "KDV'li Miktar", "Vergi Payı"))
                print("-" * 73)
                print("|{:<14s}|{:>14.2f}|{:>14.2f}|{:>14.2f}|".format(Fore.GREEN + Style.BRIGHT + "Gelirler", toplam_gelir, toplam_gelir_kdvli, gelir_vergi_payi))
                print("|{:<14s}|{:>14.2f}|{:>14.2f}|{:>14.2f}|".format(Fore.GREEN + Style.BRIGHT + "Giderler", toplam_gider, toplam_gider_kdvli, gider_vergi_payi))
                print("|{:<14s}|{:>14.2f}|{:>14.2f}|{:>14.2f}|".format(Fore.GREEN + Style.BRIGHT + "Bilanço ", toplam_gelir - toplam_gider, toplam_gelir_kdvli - toplam_gider_kdvli, kdv_ve_vergi_toplam_gelir - kdv_ve_vergi_toplam_gider))
                print("-" * 73)
                print(Style.RESET_ALL)


                sifre_dogru = False
                tekrar()
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
    sifre_dogru = True
    program()
else:
    sifre = input(Fore.RED+"Yanlış şifre(Son hak)\nŞifre Giriniz\n-->")
    if sifre == "123456":
        sifre_dogru = True
        program()
    else:
        print(Fore.RED+"Program Sonlandırılıyor")