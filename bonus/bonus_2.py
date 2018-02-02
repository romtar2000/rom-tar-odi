c = int(input("Введите температуру в градусах Цельсия: "))
try:
    float(c)
    f = 1.8*c+32
    k = c + 273
    if k<0 or k == 0:
        print("Абсолютный нуль недостижим!")
    else:
        print(f)
        print(k)
