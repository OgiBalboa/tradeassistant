# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 09:29:32 2019

@author: fener_000
"""
import tkinter
from tkinter import Label, Button, Entry, Listbox
import bin.resim
from PIL import Image,ImageTk
from bin.urunbilgi import urun
import threading
asn = tkinter.Tk()
asn.title("AISIN EXCEL ASISTAN")
asn.geometry("1000x700")
#logo = resim("pics/asnlogo.png")
logo = Image.open("pics/minilogo.png")  
logo.render = ImageTk.PhotoImage(logo)
tkinter.Label(image=logo.render).place( x = 600, y =0)
Label(text = "AISIN SATIS ASISTANI", font = ('Algerian',27)).place(x = 140, y = 20)
#-----------------------------------------FONKSİYONLAR-------------------------------------------------------
fluence = urun("Renault Fluence Sunroof")
global urunlistesi
urunlistesi = []
global nm
#def checkenter():
    #while 1 :
        
def listele():
    def ok(event):
        x = urunlistesi[0]
        try : 
            metin = "Urun Adi :" + str(x.isim) + "\n" + "Alım fiyatı   :" + str(x.afiyat) + "\nSatis Fiyatı   :" + str(x.sfiyat) + "\nStok Durumu :" + str(x.durum) + "  " + str(len(x.liste))
            Label(asn,text = metin,font = ("Arial",16)).place(x = 600, y = 150)
            
        except : 
            print("olmadi")
         
    urunler = Listbox(asn)    
    for i in range (len(urunlistesi)):
        urunler.insert(i,urunlistesi[i].isim)
    urunler.place(x = 50, y = 300)    
    urunler.bind("<Double-Button-1>", ok)

def alim():
    x = nm
    x.alim(20)  
def satis():
    x = nm
    x.satis()
def urunekle():
    global nm
    def ekle(name):
        global nm
        nm = urun(str(name))
        print("basarili")
        urunlistesi.append(nm)
        addp.destroy()
    addp = tkinter.Toplevel()
    addp.title(" URUN EKLE ")
    x = Entry(addp,width = 4)
    x.bind("<Return>", (lambda event: ekle(x.get())))
    x.pack()

Button(text = "Urünleri Listele", command = listele).place ( x = 140, y = 120)
Button(text = "Alım", command = alim).place ( x = 300, y = 120)
Button(text = "Satis", command = satis).place ( x = 400, y = 120)
Button(text = "URUN EKLE", command = urunekle).place ( x = 400, y = 200)


asn.mainloop()
