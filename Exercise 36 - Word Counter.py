import re


def count_words(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        strng = re.split(",| ", strng)

        # Or strng = strng.replace(","," ")
        #strng_list = strng.split(" ")

        return len(strng)


print(count_words("words2.txt"))

import math
print(math.cos(1))