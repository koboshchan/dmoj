bmi = lambda w, h: w / (h * h)
"""
BMI Category 	Message
More than 25 	Overweight
Between 18.5 and 25.0 (inclusive) 	Normal weight
Less than 18.5 	Underweight
"""

w,h = float(input()), float(input())
b = bmi(w,h)
if b > 25:
    print("Overweight")
elif b >= 18.5:
    print("Normal weight")
else:
    print("Underweight")