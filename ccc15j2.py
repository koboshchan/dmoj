text=input()
def check(t:str):
    happy=t.count(":-)")
    sad=t.count(":-(")
    if happy==sad==0:return("none")
    elif happy==sad:return("unsure")
    elif happy>sad:return("happy")
    elif happy<sad:return("sad")
print(check(t=text))