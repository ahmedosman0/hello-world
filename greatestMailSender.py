name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
fh = open(name)

mailsCount={}
bigNumber=0
bigMail=""

count = 0
for line in fh:
    line = line.rstrip()
    line_new = line.split()
    if line.startswith('From:'):
        mail=line_new[1]
        if mail in mailsCount:
            mailsCount[mail]=mailsCount[mail]+1
        else:
            mailsCount[mail] =1


for i in mailsCount:
    mailNew=i
    bigNew=mailsCount[i]
    bigNew=int(bigNew)

    if (bigNew>bigNumber):
        bigNumber=bigNew
        bigMail=mailNew
    else:
        continue
print(bigMail,bigNumber)
