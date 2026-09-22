# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:58:31 2026

@author: Axler0d
"""
class Shakl:
    def yuza(self):
        return 0
class Kvadrat(Shakl):
    def __init__(self,tomoni):
        self.tomoni = tomoni
    def yuza(self):
            return self.tomoni ** 2
class Doira(Shakl):
    def __init__(self,radius):
        self.radius = radius
    def yuza(self):
        return 3.14 * pow(self.radius,2)
a = int(input(("Kvadrat tomonini kiriting: ")))
shakl1 = Kvadrat(a)
r = int(input("Doira radiusini kiriting: "))
shakl2 = Doira(r)
natija1 = shakl1.yuza()
natija2 = shakl2.yuza()
print("Kvadrat yuzi: ",natija1)
print("Doira yuzi: ",natija2)