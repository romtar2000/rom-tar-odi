def countfreq():
    lexic = []
    freqdict = {}
    zapros = input("Enter word ending with -ing: ")
    if zapros.endswith('ing'):
        def counting():
            def readfile(file):
                with open(file, encoding="utf-8")as f:
                    lines = f.readlines()
                    for stroka in lines:
                        words = stroka.split()
                        for slovo in words:
                            slovo.strip(":;--"",.")
                            if slovo.endswith('ing'):
                                lexic.append(slovo)
            readfile("pride_and_prejudice.txt")
            length = len(lexic)
            print(length)
        counting()
        for word in lexic:
            if word.endswith('ing'):
                if word in freqdict:
                    freqdict[word] = freqdict[word]+1
                else:
                     freqdict[word] = 1
        print(freqdict[word])
    else:
        print("Invalid request")
countfreq()
