import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:
        userMatchingInput = input(
            "Did you mean %s instead? \n If yes then type Y, if no then type N: " %
            get_close_matches(word, data.keys())[
                0])
        if userMatchingInput == "Y" or userMatchingInput == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif userMatchingInput == "N" or userMatchingInput == "n":
            return "\nThe word doesn't exist. Please double check it."
        else:
            return "\nWe didn't understand your entry"

    else:
        return "\nThe word doesn't exist. Please double check it."


enterData = input("Please enter a word: ")
output = translate(enterData)
if (type(output)) == list:
    for item in output:
        print(item)
else:
    print(output)
