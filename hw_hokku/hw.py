# coding=utf-8
def tellvariant():
    print("1st variant")
tellvariant()
import random
def make_hokku():
    verses_set = []
    def make_verse():
        words = []
        def slovo(spisok):
            return(random.choice(spisok))
        def choice():
            with open("lexic.txt", encoding="utf-8") as file:
                lines = file. readlines()
                for stroka in lines:
                    stroka.replace("\n","")
                    spisok = stroka.split(",")
                    name = slovo(spisok)
                    words.append(name)
        choice()
        while words != []:
            if len(words) > 2:
                verse = words[0] + " " + words[1] + " " + words[2]
                words = words[3::]
            else:
                verse = words[0] + " " + words[1]
                words = []
            verses_set.append(verse)
    make_verse()
    hokku = verses_set[0] + "\n" + verses_set[1] + "\n" + verses_set[2]
    print(hokku)
make_hokku()
