def juft_sonlar(sonlar):
    juft_son = []
    for son in sonlar:
        if son == 0:
            continue
        if son % 2 == 0:
            juft_son.append(son)
    return juft_son
def juft_yigindi(sonlar):
    yigindi = 0
    for son in sonlar:
        if son % 2 == 0:
            yigindi = yigindi + son
    return yigindi
sonlar = [1,2,3,4,65,6,4,2,0,8,4,654,0,456]
juft = juft_sonlar(sonlar)
yigindi = juft_yigindi(sonlar)
print("Juft sonlar yig'indisi: ",yigindi)
print("Juft sonlar ro'yxati: ", juft)