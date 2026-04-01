burger = [461,431,420,0]
side = [100,57,70,0]
drink = [130,160,118,0]
dessert = [167,266,75,0]

print("Your total Calorie count is "+str(sum([burger[int(input())-1], side[int(input())-1], drink[int(input())-1], dessert[int(input())-1]]))+".")