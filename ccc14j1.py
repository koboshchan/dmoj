ang1,ang2,ang3 = int(input()),int(input()),int(input())
def check(x, y, z):
    if x+y+z != 180:return "Error"
    elif (x == y == z == 60) and ((x + y + z) == 180):return "Equilateral"
    elif ((x == y) or (y == z) or (x == z)) and ((x + y + z) == 180):return "Isosceles"
    else:return "Scalene"
print(check(ang1,ang2,ang3))