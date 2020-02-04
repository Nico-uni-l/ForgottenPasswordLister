import sys
from itertools import permutations
from itertools import combinations, combinations_with_replacement
import math

def header():
    print("-"*100)
    print("Forgot your own password?")
    print("Create your own password-bruteforce-list based on known letters.")
    print("Usage: python3 lister.py <known-letters> <password-length> <output-filename>")
    print("Exp.: python3 lister.py acNdB 6 pwList.txt")
    print("-"*100)
    print()

def checkInput():

    if len(sys.argv) != 4:
        print("wrong use!")
        print("Not enough arguments. See Usage.")
        exit()

    if not sys.argv[2].isdigit():
        print("wrong use!")
        print("<password-length> has to be an integer and positive.\n")
        exit()

    if int(sys.argv[2]) < len(sys.argv[1]):
        print("wrong use!")
        print("More known letters than password length.\n")
        exit()

def createAlphabet(knownLetters):
    printableLetters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
                        'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                        'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.',
                        '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ']

    lettersPW = []

    print("These are the characters used for the combination.")
    print(printableLetters)
    print("Are there some characters which are definitely not a part of the password? [y/n]\n")

    if userInput():
        print("Which ones?")
        print("Example: %\"kb8")

        chars = input()

        print("Alright. The characters "+chars+" will be removed.\n")

        for char in chars:
            printableLetters.remove(char)


    print("Are there possible duplicates of the known letters in the password?")
    print("For example: known letters: abc | password: aabc [y/n]")

    if userInput():

        return lettersPW
    else:
        for char in printableLetters:
            if char not in knownLetters:
                lettersPW.append(char)

    return lettersPW

def preCalc(knownLetters,alphabet,pwLength):
    combLen = len(list(combinations_with_replacement(alphabet, pwLength-len(knownLetters))))
    permLen = math.factorial(pwLength)

    return combLen*permLen

def wannaProceed(knownLetters,alphabet,pwLength):

    print("Your list will be around "+str(preCalc(knownLetters,alphabet,pwLength))+" passwords long.")
    print("Do you want to proceed? [y/n]")

    return userInput()

def createWordlist(alphabet,pwLength,knownLetters):

    comb = combinations_with_replacement(alphabet, pwLength-len(knownLetters))
    pwList = []

    for j in comb:
        pw = knownLetters+j
        permInside = permutations(pw)
        for k in permInside:
            pwList.append(k)
            writeToFile(k)

def writeToFile(pw):

    pw = "".join(pw)
    wordlistFile.write(pw)
    wordlistFile.write("\n")

def userInput():
    decision = input()
    decMaking = 1

    while(decMaking==1):
        if decision.lower() == "y":
            return True
        elif decision.lower() == "n":
            return False
        else:
            print("Wrong input!")
            decision = input()

if __name__ == '__main__':

    header()
    checkInput()
    knownLetters = ()
    for i in sys.argv[1]:
        knownLetters = knownLetters + (str(i),)

    alphabet= createAlphabet(knownLetters)
    pwLength = int(sys.argv[2])
    wordlistFile = open(str(sys.argv[3]), "w")

    if wannaProceed(knownLetters,alphabet,pwLength):
        createWordlist(alphabet, pwLength, knownLetters)
        wordlistFile.close()
        print("Passwords have been written to "+str(sys.argv[3])+". See ya next time.\n")

    else:
        print("Quitting. See ya next time champ.\n")
        wordlistFile.close()
        exit()







