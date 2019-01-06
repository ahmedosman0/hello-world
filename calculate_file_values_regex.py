import re

fh = open("actual.txt")
count=0
values=list()

for line in fh:
    line = line.rstrip()
    values = re.findall('([0-9]+)',line)
    for i in values:
        count=count+int(i)

print(count)

