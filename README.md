# tradeassistant
Alım ve satımlarınızı kaydeder ve yönetir.
# LOG
```python
"""
Datafinder Menu

"""
import time 
def line():
  print("*" * 50)
  
def Menu():
  global secim
  print("Menu")
  menu =  """Ne yapmak istiyorsunuz ? \n 1. Sorgula\n 2. Sürekli Çalış \n 3. Dosya Kontrol\n 4. Hata Raporları \n (Seçtiğiniz numarayı yazınız)"""
  print(menu)
  line()
  secim = int(input())
  
  if secim == 1:
    tim = time.time()
    time.sleep(1)
    fark = time.time()-tim
    print("sorgulama tamam.")
    print(float(fark))
    Menu()

Menu()
```
