with open('file.txt','a') as fayl:
    fayl.writelines(["Bekmirza\n","Ali\n","Vali\n"])
with open("file.txt") as fayl:
    fayl1 = []
    for ism in fayl:
        matn = ism.strip()
        fayl1.append(matn)
print(fayl1) 

qidiruv = input("Ism kiriting: ")
if qidiruv in fayl1:
        print("Ism topildi")
else:
        print("Topilmadi")
    
