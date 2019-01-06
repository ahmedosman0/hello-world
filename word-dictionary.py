import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def dect(word):
    word=word.lower()

    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn =input("Did you mean %s instead? enter y for Yes and n for No: " %get_close_matches(word,data.keys())[0])
        if yn =="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="n":
            return "the search doesnt match any data."

    else:
        return "word doesnt exist."
i = 1
while (i!=0):
    word=input("Enter the next word :")
    print(dect(word))

    i=int(input("If you want to search again press any key,otherwise press 0: "))

