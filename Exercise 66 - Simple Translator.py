
d = dict(weather = "clima", earth = "terra", rain = "chuva")

def translate(key):
    try:
        return d[key]
    
    except KeyError:
        return "word wasnt found"


word=input("Enter the word you want to transelate to Portuguese : ")

print(translate(word))


