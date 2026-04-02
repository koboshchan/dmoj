one = len([[]])
five = len([[], [], [], [], []])
ten = five * (one + one)

seventy_two = ten * (five + one + one) + one + one
one_hundred_one = ten ** (one + one) + one
one_hundred_eight = one_hundred_one + ten - one - one - one
one_hundred_eleven = one_hundred_one + ten
forty_four = ten * (five - one) + five - one
thirty_two = ten * (one + one + one) + one + one
eighty_seven = ten * (five + one + one + one) + five + one + one
one_hundred_fourteen = ten ** (one + one) + ten + five - one
one_hundred = ten ** (one + one)
thirty_three = thirty_two + one

print(chr(seventy_two) + chr(one_hundred_one) + chr(one_hundred_eight) + chr(one_hundred_eight) + chr(
    one_hundred_eleven) + chr(forty_four) + chr(thirty_two) + chr(eighty_seven) + chr(one_hundred_eleven) +
      chr(one_hundred_fourteen) + chr(one_hundred_eight) + chr(one_hundred) + chr(thirty_three))