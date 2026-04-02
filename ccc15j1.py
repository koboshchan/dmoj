month,day=int(input()),int(input())
def check(m,d):
    if month == 2 and day == 18:return("Special")
    elif month < 2:return("Before")
    elif month == 2 and day < 18:return("Before")
    elif month > 2:return("After")
    elif month == 2 and day > 18:return("After")
print(check(m=month,d=day))