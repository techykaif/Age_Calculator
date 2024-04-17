import datetime
dob=str(input("Enter Your Date of Birth(DD/MM/YYYY):"))
dob=dob.replace('/','')
if dob.isdecimal()==False:
    print("Invalid Date of Birth")
    exit(0)
try:
    dob_day=int(dob[0]+dob[1])
    dob_month=int(dob[2]+dob[3])
    dob_year=int(dob[4]+dob[5]+dob[6]+dob[7])
except:
    print("Invalid Date of Birth")
    exit(0)
def verifyInputs():
    if dob_day>31:
        print("a Month Cannot have more than 31 days")
        exit(0)
    if dob_month>12:
        print("A Year Cannot have More than 12 months")
        exit(0)
    else:
        ageCalculator()
def ageCalculator():
    day=datetime.date.today().day
    month=datetime.date.today().month
    year=datetime.date.today().year 
    if day>=dob_day:
        day=day-dob_day
    else:
        if month==1 or month==3 or month==5 or month==12 or month==10 or month==8 or month==7:
            day+=31
            if(month==1):
                year=year-1
                month=12
            else:
                month-1
        if month==2 and year%4==0:
            day+=29
            month-1
        if month==2:
            day+=28
            month-1
        else:
            day+=30
            month-=1
        day=day-dob_day
    if month>=dob_month:
        month=month-dob_month
    else:
        month+=12
        year-=1
        month=month-dob_month
    if month>12:
        month-=12
        year+=1

    year=year-dob_year
    if year==0:
        print("Your Age is :",month,"Months",day,"Days")
    else:
        print("Your age is : ",year,"Years",month,"Months",day,"Days")

verifyInputs()      

        
