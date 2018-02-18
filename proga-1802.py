import random
def wordgame():
    questionnaire = {}
    wordlist = []
    answersheet = []
    def check_answer(user_answer, right_answer):
        if user_answer == right_answer:
            print("This answer is right! You won!")
        else:
            print("This answer is not right")    
    def makequestion():   
        def makedict(file):
            with open (file, encoding="utf8") as f:
                lines = f.readlines()
                for stroka in lines:
                    cells = stroka.split(",")
                    question = cells[0]
                    answer_ = cells[1]
                    answer = answer_.strip("\t\n")
                    questionnaire[question] = answer 
                for k in questionnaire:
                    wordlist.append(k)
                    answersheet.append(questionnaire[k])
        makedict("wordlist.csv")
        random.shuffle(wordlist)
    makequestion()
    request = wordlist[0]
    right_answer = questionnaire[request]
    number_of_guesses = len(right_answer)
    print(request, "...")
    print("You will be given ",number_of_guesses,"attempts, as much as letters in this word")
    user_answer = input("Enter your answer: ")
    check_answer(user_answer, right_answer)
    while user_answer != right_answer :
            number_of_guesses = number_of_guesses - 1
            if number_of_guesses > 1:
                print("Try again.")
                print(number_of_guesses, "attempts remained")
                user_answer = input("Enter your answer: ")
                check_answer(user_answer, right_answer)
            elif number_of_guesses == 1:
                print("Try again.")
                print("Last attempt")
                user_answer = input("Enter your answer: ")
                check_answer(user_answer, right_answer) 
            else:
                print("This is a wrong answer! You ran out of attempts and lost!")
                break
    print(right_answer)
wordgame()
    
