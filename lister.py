'''
(c) https://github.com/Nicolas-le (2020)
'''

import sys
from itertools import permutations
from itertools import combinations, combinations_with_replacement
import math

def header():
    '''
    Prints the terminal-header. Short explanation on how to use it.
    :return: nothing
    '''
    print("-"*100)
    print("Forgot your own password?")
    print("Create your own password-bruteforce-list based on known letters.")
    print("Usage: python3 lister.py <known-letters> <password-length> <output-filename>")
    print("Exp.: python3 lister.py acNdB 6 pwList.txt")
    print("-"*100)
    print()

def checkInput():
    '''
    Checks the command input and exits if something is wrong.
    Improvable through try.
    :return:
    '''
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
    '''
    Create the list of letters the already known letters will be combined with.
    Out of these combinations the permutations are created.
    Checks for some decisions of the user. See down below.
    :param knownLetters: tuple with all the already known letters. Not a list because of
    addition in the createWordlist() function.
    :return: printableLetters --> these are are all letters which are combined with the known
    letters after some changes, based on the user decision.
    '''
    printableLetters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
                        'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                        'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.',
                        '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ']

    '''
    Prints all letters which could be used for a password.
    '''
    print("These are the characters used for the combination.")
    print(printableLetters)
    print("Are there some characters which are definitely not a part of the password? [y/n]")

    '''
    User decides if some characters are definitely not a part of the password.
    The function userInput() is used to decide if yes or no and afterwards, based on
    this decision, the chosen characters are removed from the printableLetters list.
    '''
    if userInput():
        print("Which ones?")
        print("Example: %\"kb8")

        chars = input()

        print("Alright. The characters "+chars+" will be removed.\n")

        for char in chars:
            printableLetters.remove(char)


    print("Are there possible duplicates of the known letters in the password?")
    print("For example: known letters: abc | password: aabc [y/n]")

    '''
    If there could be duplicates in the password of the known letters, nothing is changed.
    If not, the known letters are removed from the alphabet to save some calculation time.
    '''
    if userInput():
        return printableLetters
    else:
        for char in printableLetters:
            if knownLetters.__contains__(char):
                printableLetters.remove(char)

    return printableLetters

def wannaProceed(knownLetters,alphabet,pwLength):
    '''
    Asks if the user wants to proceed. Maybe not if the password count is already to high.
    Then some things like the alphabet can be adjusted. Uses the function preCalc to estimate
    the passwords.
    :param knownLetters:    tuple with all the already known letters.
    :param alphabet:        all the letters the known letters will be combined wit
    :param pwLength:        length of the password
    :return:
    '''
    print("Your list will be around "+str(preCalc(knownLetters,alphabet,pwLength))+" passwords long.")
    print("Do you want to proceed? [y/n]")

    return userInput()

def preCalc(knownLetters, alphabet, pwLength):
    '''
    Calculates how many passwords are possible and will be calculated.
    This is meant to be as an indicator if the possibilities are to many.
    Calculation:    combinations of the alphabet (dependent on the password length)
                *   factorial of the password length (permutations of the password)

                f.ex.   pwLength = 3 --> so 3! = 6 (6 possibilities)
                        knownLetters = ad
                        combinations are only one element of the alphabet
                        so every element of the alphabet is combined with ad and out of
                        that all permutations are calculated

                        len(alphabet) * 6

    :param knownLetters:    tuple with all the already known letters.
    :param alphabet:        all the letters the known letters will be combined with
    :param pwLength:        length of the password
    :return:                password counter
    '''

    combLen = len(list(combinations_with_replacement(alphabet, pwLength - len(knownLetters))))
    permLen = math.factorial(pwLength)

    return combLen * permLen

def createWordlist(alphabet,pwLength,knownLetters):
    '''
    Create the wordlist out of all combinations of the alphabet + known letters.
    For each combination + knownletters the script calculates all permutations.
    These are written to a file.
    F.ex.   alphabet (a,b) --> combinations (a,a);(a,b);(b,b)
            pwLength = 3, knownLetters = c
            (a,a) + (c) --> all permutations
            (a,b) + (c) --> all permutations
            (b,b) + (c) --> all permutations

    :param alphabet:        all the letters the known letters will be combined with
    :param pwLength:        length of the password
    :param knownLetters:    tuple with all the already known letters.
    :return:
    '''

    comb = combinations_with_replacement(alphabet, pwLength-len(knownLetters))
    pwList = []

    for j in comb:
        pw = knownLetters+j
        permInside = permutations(pw)
        for k in permInside:
            pwList.append(k)
            writeToFile(k)

def writeToFile(pw):
    '''
    Simple filewriter.
    Joins tuple to string and writes string password to file.
    :param pw:  password tuple f.ex. ("a","b","d")
    :return:    nothing
    '''

    pw = "".join(pw)
    wordlistFile.write(pw)
    wordlistFile.write("\n")

def userInput():
    '''
    Asks for user input if yes or no.
    :return: True if yes and False if no
    '''
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
    '''
    Whole script process.
    '''

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







