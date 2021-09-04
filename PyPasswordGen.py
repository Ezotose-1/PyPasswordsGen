__author__ = 'Ezotose'


## Customs Package ##
import random
import sys


## Functions ##
def __input(prompt=""):
    if (sys.version_info[0] == 3):
        return input(prompt)
    else:
        return raw_input(prompt)

def _headerMain(txt):
    str = "---------------------------------------------------\n"
    for s in txt:
        str += "--------"
        str +=" " * ((36-len(s))//2)
        str += s
        str +=" " * ((35-len(s))//2)
        str += "--------\n"
    str += "---------------------------------------------------"
    print(str)


letters = "azertyauiopqsdfghjklmwxcvbn"
numbers = "01234056789"
symbols = "&\"\(&-_@\\)~#\{[|@]\}/*$%:;+"
allChar = letters + letters.upper() + numbers + symbols

lettersLen = len(letters)-1
numbersLen = len(numbers)-1
symbolsLen = len(symbols)-1
allLen = len(allChar)-1

    # Reccurent Minimal : upper and lowercase alphabetical, number, symbol
def _generation(Charmax):
    GenPass = ""
    GenPass += letters[random.randint(1, lettersLen)]
    GenPass += (letters[random.randint(1, lettersLen)]).upper()
    GenPass += symbols[random.randint(1, symbolsLen)]
    GenPass += numbers[random.randint(1, numbersLen)]
    for i in range(int(Charmax)-4):
        GenPass += allChar[random.randint(1, allLen)]
    return GenPass
    


## Main Function ##
def main():
    _headerMain(["Python Password Generator", "By Ezotose"])
    Charmax = " "
    while not(Charmax.isnumeric()) or int(Charmax)<4: 
        Charmax = __input("How many characters (at least 4) ?\n> ")
        if not(Charmax.isnumeric()) or int(Charmax)<4:
            print("Please enter a correct value (at least 4).\n")
    GenPass = _generation(Charmax)
    print("Generated password :\n"+GenPass)
    return GenPass


## Main ##
main()

# build with Python 3.6.9 #
