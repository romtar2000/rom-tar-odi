def readfile(file):
    with open(file, encoding="utf-8") as f:
        text = f.read()
    return text

def searchwords(text):
    sentences = text.replace('?', '.').replace('!', '.').replace('...', '.').split('.')
    words = [phrase.split() for phrase in sentences]
    for words_internal in words:
        slova = [word.strip(',;:""«»()[]-') for word in words_internal]
        answers = [slovo for slovo in slova if len(slovo) > 7]
    return answers

def printnormally(spisok):
    for item in spisok:
        sym = '-'
        if len(item) < 10:
            coeff = 20 - len(item)
        else:
            coeff = 19 - len(item)
        pad = sym * coeff
        line = '{}{}{}'.format(item, pad, len(item))
        print(line)

    

printnormally(searchwords(readfile('ostrovskiy.txt')))
