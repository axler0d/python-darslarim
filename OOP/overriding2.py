# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:13:34 2026

@author: Axler0d
"""

class Xodim:
    def __init__(self,ism,maosh):
        self.ism = ism
        self.maosh = maosh
    def malumot(self):
        return f"{(self.ism).capitalize()} ismli odam {self.maosh} so'm maosh oladi"
class Menejer(Xodim):
    def __init__(self, ism, maosh,jamoa_soni):
        super().__init__(ism, maosh)
        self.jamoa_soni = jamoa_soni
    def malumot(self):
        asosiy = super().malumot()
        return f"{asosiy}, {self.jamoa_soni} sonli brigadani boshqaradi"

ism = input("Ismingizni kiriting: ")
while not ism.isalpha():
    print("Ismingizda raqam qatnashgan, iltimos uni qayta kiriting😊")
    ism = input("ismingizni qayta kiriting...: ")
menejr = Menejer(ism, 8000000,10)
print(menejr.malumot())