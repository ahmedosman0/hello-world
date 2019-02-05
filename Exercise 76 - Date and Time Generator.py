import datetime

x=datetime.datetime.now().strftime("%A,%B,%d/ %m/ %Y")
print(x)
old=int(input("how old are you? : "))
currentYear = datetime.datetime.now().strftime("%Y")
currentYear=int(currentYear)

bornDate=currentYear-old
print("you were born in ",bornDate)



# We're using datetime  standard module here which supplies classes to manipulate dates and times.
# Note that datetime.now()  would produce 2016-12-25 22:54:34.153209 which is a datetime  object.
# However, by applying strftime (string from time) we convert that object to a readable string using format codes.
# For example, %A  would extract the day, %B  the month, %d  the date, and %Y  the year.
# You can find the complete list of format codes in the strftime.org website.
