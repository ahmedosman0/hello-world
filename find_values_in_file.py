#file name is mbox-short.txt
fname = input("Enter file name: ")
fh = open(fname)
count = 0
add = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        number = line[20:26]
        number = float(number)
        count = count + 1
        add = add + number

average = add / count
print("Average spam confidence:", average)