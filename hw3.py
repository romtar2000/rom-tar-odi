print("1st variant")
word=list(input("Enter word: "))
if word:
    for i,sym in enumerate(word):
        word=word[:-1]
        word1="".join(word)
        print(word1)
    print ("No more symbols")
else:
    print ("Enter at least one symbol")
