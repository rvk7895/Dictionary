import json
from difflib import SequenceMatcher
from difflib import get_close_matches
import configparser

configParser = configparser.RawConfigParser()
configFilePath = "./config.cfg"
configParser.read(configFilePath)

jsonFilePath = configParser.get("info", "jsonFilePath")

data = json.load(open(jsonFilePath))


# function which takes word as an argument and returns its meaning
def translate(w):
    global word
    global data
    try:
        for meaning in data[w]:
            print(meaning)
        return

    except:
        d = get_close_matches(w, data.keys(), 5, 0.7)
        if len(d) > 0:
            print("Did you mean any of these words")
            for x in d:
                print("{}".format(x), end=" ")
            choice = input("\nEnter y or n : ")
            choice = choice.lower()

            if choice == 'y':
                word = input("Enter the word : ")
                translate(word)

            else:
                print("Wrong word!! Please try again.")

        else:
            print("The word doesn't exist please double check it.")


word = input("Enter the word : ")
word = word.lower()
translate(word)
