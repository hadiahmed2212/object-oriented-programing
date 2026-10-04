def calculate_change(paid, price):
    change = paid - price
    return change
 
ticket_price = 30
print("PARKING TICKETS")
print("parking tickets cost:$",ticket_price)
print("accepted coins: 20c, 5c, 10c, 50c")
 
total_inserted = 0
coins_inserted = 0
while True:
    coin = int(input("Insert a coin (1, 5, 10, or 25): "))
    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid coin, try again")
        continue 
 
    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted {coin}. Total so far: {total_inserted}\n")
 
    if total_inserted >= ticket_price:
        print("correct amount of money inserted")
        break

change_due = calculate_change(total_inserted, ticket_price)
 
print("ticket printing:)")

if change_due == 0:
    pass
else:
    print(f"change: {change_due}")