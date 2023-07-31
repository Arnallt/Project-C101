import random
#⚀⚁⚅⚃⚄⚂

response = 'y'


while response == 'y':
    
    number = random.randint(0,6)

    if(number == 1):
        print("[       ]")
        print("[   O   ]")
        print("[       ]")
    if(number == 2):
        print("[O      ]")
        print("[       ]")
        print("[      O]")
    if(number == 3):
        print("[O      ]")
        print("[   O   ]")
        print("[      O]")
    if(number == 4):
        print("[O     O]")
        print("[       ]")
        print("[O     O]")
    if(number == 5):
        print("[O     O]")
        print("[   O   ]")
        print("[O     O]")
    if(number == 6):
        print("[O     O]")
        print("[O     O]")
        print("[O     O]")

    question = input("Roll Dice Y/N?")

