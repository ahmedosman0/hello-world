x=input("Enter The Number:")
is_bigger=0
is_smaller=0
while x!="done":

    try:
        x=int(x)
    except:
        print("Enter Intger!")
        x = input("Enter The Number:")
        x = int(x)
    if is_smaller == 0:
        is_smaller=x
    if x>is_bigger:
        is_bigger=x
    if x<is_smaller:
        is_smaller=x

    x=input("Enter The Number:")
print("Maximum is",is_bigger)
print("Minimum is",is_smaller)