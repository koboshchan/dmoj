"""
km/h over the limit 	Fine
1 to 20 	$100
21 to 30 	$270
31 or above 	$500
"""

limit = int(input())
speed = int(input())

if speed <= limit:
    print("Congratulations, you are within the speed limit!")
else:
    over = speed - limit
    if over <= 20:
        print("You are speeding and your fine is $100.")
    elif over <= 30:
        print("You are speeding and your fine is $270.")
    else:
        print("You are speeding and your fine is $500.")