import datetime

#restore current datetime
currentDate=datetime.datetime.now()
currentDatestr=str(currentDate)

#create file with date name
def create_file(note):
    with open(currentDate.strftime("%Y-%m-%d-%I-%M-%p")+".txt","w+") as file:
        file.write(currentDatestr+"\n\n"+note)

        #restore file name
        fileName=file.name
        return fileName

#take text from user
note=input("enter your note:")


fileName=create_file(note)
print(fileName)