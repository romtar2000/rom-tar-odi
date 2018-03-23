import re

def readfile(file):
    with open (file, encoding="utf-8") as f:
        text = f.read()
    return text

def searchverb(text):
    answer = re.findall('((откроют?)|(открое[мшт][еь]?)|(откры[вл](ши)?й?)|(открой(те)?))(с[яь])?',text)
    return answer

def listforprint(massive):
    listforprint = []
    for intern_massive in massive:
        while len(intern_massive) > 0:
            if not intern_massive[0] in listforprint:
                listforprint.append(intern_massive[0])
            intern_massive = intern_massive[1::]
    return listforprint

def printnormally(massive):
    while len(massive) > 0:
        print(massive[0])
        massive = massive[1::]

print(listforprint((searchverb(readfile("ostrovskiy.txt")))))
