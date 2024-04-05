class Ucus:


   def havayolu(self):
       print("THY")

   def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
       self.kod = kod
       self.kalkis = kalkis
       self.varis = varis
       self.sure = sure
       self.kapasite = kapasite
       self.yolcu = yolcu

   def get_ucus(self, kod_ismi):
       if kod_ismi == "TK532":
           print(ucus1.kod)
           print(ucus1.kalkis)
           print(ucus1.varis)
           print(ucus1.kapasite)
       else:
           print("bok")



ucus1 = Ucus("TK532", "IST", "ANK", 60, 300, 21)
ucus2 = Ucus("TK112", "ADB", "ANT", 51, 212, 14)

print(ucus1.varis)





