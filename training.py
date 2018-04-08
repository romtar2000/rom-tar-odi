import re

def readfile(file):
    with open(file, encoding="utf-8") as f:
        text = f.read()
    return text

def search_dze(text):
    dze = re.findall('title=".+?дзе, .+?">', text)
    return dze

def search_svili(text):
    svili = re.findall('title=".+?швили, .+?">', text)
    return svili

def coefficient(L1, L2):
    coefficient = L1/L2
    return coefficient

print(coefficient(len(search_dze(readfile("Georgians.html"))), len(search_svili(readfile("Georgians.html")))))

def count_ia(text):
    ia = re.findall('title=".+?ия, .+?">', text)
    L0 = len(ia)
    return L0

print(count_ia(readfile("Georgians.html")))

def replacement(massive):
    with open("0804.txt", 'a', encoding="utf-8") as f:
        for item in massive:
            item.replace('title=', '')
            info = item.split(",")
            data = info[1]
            names = data.split()
            if len(names[0]):
                names[0].replace(names[0], "Галактион")
                "".join(item)
                f.write(item)

replacement(search_dze(readfile("Georgians.html")))
replacement(search_svili(readfile("Georgians.html")))
