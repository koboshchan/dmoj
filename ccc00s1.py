"""
Martha takes a jar of quarters to the casino with the intention of becoming rich. 
She plays three machines in turn. Unknown to her, the machines are entirely predictable. 
Each play costs one quarter. 
The first machine pays 30 quarters every 35 t h time it is played; 
the second machine pays 60 quarters every 100 t h time it is played; 
the third pays 9 quarters every 10 t h time it is played.
"""

number_of_quarters = int(input())
machine_last_paid = [int(input()) for _ in range(3)]

def next_payment(machine):
    if machine == 0:
        return 30, 35
    elif machine == 1:
        return 60, 100
    else:
        return 9, 10

times_before_going_broke = 0

while number_of_quarters > 0:
    for machine in range(3):
        if number_of_quarters == 0:
            break
        times_before_going_broke += 1
        number_of_quarters -= 1
        payment, period = next_payment(machine)
        machine_last_paid[machine] += 1
        if machine_last_paid[machine] == period:
            number_of_quarters += payment
            machine_last_paid[machine] = 0

print(f"Martha plays {times_before_going_broke} times before going broke.")