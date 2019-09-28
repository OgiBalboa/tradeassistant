# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:48:16 2019

@author: fener_000
"""
import sqlite3
import tkinter
from tkinter import Label,Tk,Button,Entry
import time

class urun():
    def __init__(self,name):
        self.isim = name
        #self.ID
        self.kar = 50
        self.sayi = 0
        self.liste = []
        self.stokliste=[] # siparis : Sipariş Verildi |yolda : Kargoda |var: Stokta Bulunuyor
        self.start = True
        self.stok()
    def stok(self,):
        try: 
            self.afiyat = int(self.liste[0])
            self.sfiyat = int(self.afiyat) + int(self.kar)
        except : 
            self.durum = "yok"
            if self.start == False:
                print("ÜRÜN ŞU ANDA BULUNMAMAKTA")
            self.afiyat = 0
            self.sfiyat = 0
        #self.no = no
        if len(self.liste) >0 :
            self.durum = "var"
    def gelenurun(self,):
        pass
    def alim(self,fiyat):
        self.start = False
        self.liste.append(fiyat)
        self.stokliste.append("siparis")
        self.stok()
    def satis(self,):
        self.liste.pop(0)
        self.stokliste.pop(0)
        
        self.start = False
        
        print("SATIŞ YAPILDI ! ")
        print("\nKalan Ürün : "+ str(len(self.liste)))
        self.stok()


def listele(x):
    metin = "Urun Adi :" + str(x.isim) + "\n" + "Alım fiyatı   :" + str(x.afiyat) + "\nSatis Fiyatı   :" + str(x.sfiyat) + "\nStok Durumu :" + str(x.durum) + "  " + str(len(x.liste))
    print(metin)
    print("*" * 30)

def satis(x):
    x.satis()

def alim(x,y):
    x.alim(y)
    
print("\nHOŞ GELDİNİZ !\n\n")
"""
while 1:
    a = str(input("Ne yapacaksın ? (listele,alim,satis,cikis) ")) 
    print("*" * 30)
    if a == "listele":
        time.sleep(1)
        listele(fluence)
    if a == "alim":
        time.sleep(1)
        b = int(input("Kaç TL ? "))
        alim(fluence,b)
    if a == "satis":
        time.sleep(1)
        satis(fluence)
    if a == "cikis":
        print(" GÖRÜŞMEK ÜZERE ! ")
        time.sleep(1)
        break

"""

