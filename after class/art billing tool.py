def greet_customer():
    print("Welcome to the Art Supplies Store!")
    print("Get your colours, brushes, and paper here.")

greet_customer()
 

price_per_item = float(input(" price per art item? "))
items_bought = int(input("number of items bought: "))
def calculate_total(price, items):
    total = price * items
    return total
total_cost = calculate_total(price_per_item, items_bought)
 
rounded_total = round(total_cost, 2)
print("Total Cost:", rounded_total)
amount_paid = float(input(" paid? "))
 
def calculate_change(paid, total):
    change = paid - total
    return change
 
change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

def thank_you_msg(items):
    if items >= 5:
        return "good sence of taste"
    else:
        return "thank you!"

closing_message = thank_you_msg(items_bought)
