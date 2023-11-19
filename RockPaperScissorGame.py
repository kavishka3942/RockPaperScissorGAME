import random

try:
    choicesList = ["rock", "paper", "scissor"]
    rock = {"scissor": "Gotcha...!", "paper": "I missed it..!"}
    paper = {"rock": "Gotcha...!", "scissor": "I missed it..!"}
    scissor = {"paper": "Gotcha...!", "rock": "I missed it..!"}

    human = input("rock, paper or scissors..? ").lower()
    while human in choicesList:
        choicesList = ["rock", "paper", "scissor"]
        computer = random.choice(choicesList)

        if human == computer:
            print("player :" + human)
            print("computer :" + computer)
            print("Tie...! Good for you!")
        elif computer == "rock":
            print("player :" + human)
            print("computer :" + computer)
            result = rock[human]
            print(result)
        elif computer == "paper":
            print("player :" + human)
            print("computer :" + computer)
            result = paper[human]
            print(result)
        elif computer == "scissor":
            print("player :" + human)
            print("computer :" + computer)
            result = scissor[human]
            print(result)
        else:
            break
        human = input("rock, paper or scissors..? ").lower()

    print("ohh.. you giving up..GG")

except :
    print("something went wrong")

