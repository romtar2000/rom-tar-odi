slovo = input("Enter word: ")
list= []
if slovo == "":
    print("No word entered")
else:
    while slovo != "":
        list.append(slovo)
        slovo = input("Enter word: ")
with open ("proga.txt", "w", encoding="utf-8") as f:
    for element in range(len(list)):
        word = list[element]
        u = ""
        for item in range(len(word) -1, -1, -1):
            u = u+word[item]
        for item in range(len(u)):
            if((item+1)%3) != 0:
                f.write(u[item])
        f.write("\n")

    
