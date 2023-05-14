import datetime

# print(datetime.date.today())
def cal_age(year,month,day):
    today = datetime.date.today() # This will give today's date
    dob = datetime.date(year,month,day)
    # To calculate the age
    age = int((today-dob).days/365)
    # print(age)
    # line 8,9 and 11 will return the correct age in integer
# cal_age(2000,10,20)
    
    # How to ask users to enter their age
    
    return age

user_dob = input("Enter your D.O.B in this format 'Year-month-day': ")
dob = user_dob.split('-')

# print(dob) will return our input in string like this : ['1994', '12', '24']
year,month,day = int(dob[0]), int(dob[1]), int(dob[2])
your_age = cal_age(year,month,day)
print(f"You are {your_age} years old.")