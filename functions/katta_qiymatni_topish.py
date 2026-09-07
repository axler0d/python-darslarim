def eng_katta(sonlar):
    max_son = sonlar[0]

    for i in sonlar:
        if i > max_son:
            max_son = i

    return max_son


numbers = [-10, -5, -2, -20]

natija = eng_katta(numbers)

print(natija)


