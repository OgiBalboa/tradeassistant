"""
Data finder MENU
author = @ogibalboa

"""
print("Yükleniyor...")
import time
from time import sleep
sleep(0.2)
print("Time lib içeri aktarıldı.")
import os
print("Os lib içeri aktarıldı.")
import bin.verianaliz as verianaliz
sleep(0.2)
print("veri analiz modülü içeri aktarıldı")
def line(x):
    print("*" * x)
def vertline(x,y):
    lin = "*" + " "*y +"*\n"
    print(lin*x)
line(52)
def wt():
    sleep(0.5)
def clr():
    os.system("clear")
print("* MERHABA ! \n* Datafinder Programına hoş geldiniz !             *")
vertline(1,50)
line(52)
def enter():
    input("\nDevam etmek icin Enter'a basınız")
enter()
global emp
emp = []
for i in range(0,50):
    emp.append(i)

global a
a = 0
def sorgular():
    global a
    global sorgu
    if sorgu == 1:
        print("Dosya Kontrol")
        wt()
        enter()
        Menu()
    elif sorgu == 2:
        emp[a] = verianaliz.sorgu()
        verianaliz.dosya_aktar(emp[a].dosya,emp[a].dosya_yolu)
        line(50)
        print("Sorgu tamamlandı.\n")
        a+=1
        line(52)
        gir = int(input("1. Aynı dosyadan başka sorgu \n2.Farklı Tarihe git\n3.Ana Menü\n"))
        if gir == 1:
            emp[a-1].search()
            gir = int(input("1. Aynı dosyadan başka sorgu \n2.Farklı Tarihe git\n3.Ana Menü\n"))
            wt()
            sorgu = 2
            sorgular()
        if gir == 2:
            
            emp[a] = verianaliz.sorgu()
            verianaliz.dosya_aktar(emp[a].dosya,emp[a].dosya_yolu)
            gir = int(input("1. Aynı dosyadan başka sorgu \n2.Farklı Tarihe git\n3.Ana Menü\n"))
            wt()
            sorgu = 2
            sorgular()
        if gir == 3:
            wt()
            clr()
            enter()
            Menu()
            
        Menu()   
    elif sorgu == 3:
        print("Error Logları : \n")
        anlik = os.getcwd()
        os.chdir('Errors')
        hatalar = os.listdir()
        cout = 0
        for i in hatalar:
            cout+=1
            print("Dosya No  :" + str(cout) + "  Dosya Adı : "+ i)
            print('\n')
        goruntule = int(input("Görüntülemek istediğiniz dosya No : "))
        dosya = open(hatalar[goruntule - 1],'r')
        print(dosya.read())
        os.chdir(anlik)
        wt()
        enter()
        Menu()

def Menu():
    line(52)
    ask = """Ne yapmak istiyorsun ?\n\n1. Otomatik Dosya Kontrol\n\n2. Dosya Sorgula \n\n3. Hataları Görüntüle \n\n"""
    print(ask)
    line(50)
    global sorgu
    sorgu =  int(input("Seçiniz \t :  "))
    line(50)
    clr()
    sorgular()

Menu()
