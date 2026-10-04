
def total_bill(bill_amount, tip_perc):
    total = bill_amount * (1 + 1 * tip_perc)
    total = round(total, 2)
    print(f"pay ${total} to play")
    return total
total_bill(150, 20)
def seating_arrangements(guests):
    '''This is a function to find the number of arrangements'''
 
    
    if guests == 0 or guests == 1:
        return 1
    else:
        return guests * seating_arrangements(guests - 1)
 
print(seating_arrangements.__doc__)
print("Seating for 1 guest:", seating_arrangements(1))
print("Seating for 2 guests:", seating_arrangements(2))
print("Seating for 3 guests:", seating_arrangements(3))
print("Seating for 5 guests:", seating_arrangements(5))
