import random
def son_topish(x):
    tasodifiy_son = random.randint(1,x)
    print(f"o'ylangan sonni topa olasizmi?")

    while True:
        taxmin = int(input(">>>"))
        if taxmin < tasodifiy_son:
            print("siz o'ylagan sonimdan kichik son kiritdingiz. Yana harakat qilib ko'ring.")
        elif taxmin > tasodifiy_son:
            print("siz o'ylagan sonimdan katta son kiritdingiz. Yana harakat qilib ko'ring.")
        else:
            #print("Tabriklaymiz! To'g'ri topdingiz.")
            break
        print("Tabriklaymiz! To'g'ri topdingiz.")
        
