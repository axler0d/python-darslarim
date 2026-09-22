# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:16:44 2026

@author: Axler0d
"""

class Hayvon:
    def __init__(self,nom):
        self.nom = nom
    
    def tavsif(self):
        return f"Men {self.nom} ismli hayvonman"
class It(Hayvon):
    def __init__(self,nom,zot):
        super().__init__(nom)
        self.zot = zot
    def tavsif(self):
        ota_tavsif = super().tavsif()
        return f"{ota_tavsif}, zotim {self.zot}"
class Kuchukcha(It):
    def __init__(self,nom,zot,yosh):
        super().__init__(nom, zot)
        self.yosh = yosh
    def year(self):
        return f"{self.nom} ismli kuchuk yoshi {self.yosh} yoshda"
#yosh = int(input("Itning yoshini kiriting: "))
kuchuk = Kuchukcha("olapar", "daydi",2)
it = It("Rex", "Nemis cho'poni")
print(it.tavsif())
print(kuchuk.tavsif())
print(kuchuk.year())       
            