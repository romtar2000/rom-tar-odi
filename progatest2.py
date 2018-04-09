import re

def readfile(file):
    with open(file, encoding="utf-8") as f:
        text = f.read()
    return text

def headlines_number(text):
    massive = []
    lines = text.split("\n")
    for line in lines:
        if not re.search('<teiHeader>', line):
            massive.append(line)
        else:
            massive.append(line)
            break
    return len(massive)

def makedict(text):
    dictionary = {}
    answer = re.findall('<w lemma=".+?" type="(.+?)"', text)
    for item in answer:
        if item in dictionary:
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return dictionary
    

def main(dictionary):
    with open("task.txt", 'a', encoding="utf-8") as f:
        f.write(str(headlines_number(readfile("f.xml"))))
        for i in dictionary:
            f.write(str(i) + "-" + str(dictionary[i]))

main(makedict(readfile("f.xml")))
