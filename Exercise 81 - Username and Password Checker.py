while True:
    usr = input("Enter New Username: ")
    with open("user.txt","r") as file:
        user = file.readlines()
        users = [i.strip("/n") for i in user]
    if usr in users:
        print("Username Exists")
        continue
    else:
        print("Username If fine")
        with open("user.txt","w") as filew:
            filew.write(usr)
            break

while True:
    notes = []
    psw = input("Enter password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)