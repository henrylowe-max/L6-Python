from datetime import datetime

today = datetime.now()
birthdate = datetime(int(input("birth year?")),int(input("birth month")),int(input("birth day")))

print(f"todays date: {today.strftime("%d-%b-%Y")}")
print(f"your birthdate: {birthdate.strftime("%d-%b-%Y")}")
print(f"current time: {today.strftime("%H:%M")}")

years = today.year - birthdate.year
months = today.month - birthdate.month
if months < 0:
    years -=1
    months +=12
    
print(f"your age: {years} and {months} months")