_,votes=input(),input()
def check(votes):
    if votes.count("A")==votes.count("B"):return "Tie"
    elif votes.count("A")<votes.count("B"):return "B"
    elif votes.count("A")>votes.count("B"):return "A"
print(check(votes=votes))