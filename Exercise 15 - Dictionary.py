#create dictionary and sum the
dic = {"a": 1, "b": 2, "c": 3, "d": 4}

print(dic["a"]+dic["b"])
dic["e"] = 5
print(dic)
for item in dic:
    print(dic[item])

def calc(dic):
    calc = (sum(dic.values()))
    return calc


dicSum = calc(dic)
print("dic sum = ", dicSum)

# remove keys that its value bigger than 3
dic = dict((key, value) for key, value in dic.items() if value <= 3)
print(dic)

#create keys with multible values and print them
d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
print(d["b"][2])

for key,value in d.items():
    print(key,"has values",value)

#print alphapits
import string
for letter in string.ascii_lowercase:
    print(letter)