#Self-Assessment Q's
#1. The first bug I spotted was that the total was being replaced by each sale instead of adding all the sales together. I learned that I need to pay closer attention to how variables change inside loops and use print statements to help me find mistakes. This showed me that I am still developing my debugging skills, but I am learning how to identify and fix errors.
#2. The apply_discount(price, tier) function takes the price of something and the customer's membership level. If they have gold, they get 15% off; silver gets 10% off; and bronze gets 5% off. If they don't have a membership, they pay the full price. A coworker could use this function without reading all the code because they just need to know the price and the membership level.
#3. "# I used AI to help me understand Python concepts and clarify error messages so I could improve my own problem solving and debugging skills." I feel like it built my understanding because I learned why the code was wrong instead of just copying the correct code.

# Exercise 1 
def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

#Exercise 2 
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

price = 200

print(f"gold:   ${apply_discount(price, 'gold'):.2f}")
print(f"silver: ${apply_discount(price, 'silver'):.2f}")
print(f"bronze: ${apply_discount(price, 'bronze'):.2f}")
print(f"none:   ${apply_discount(price, 'none'):.2f}")

# Exercise 3
def calculate_tax(price, rate):
    return price * rate

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

price = 200

discounted = apply_discount(price, "gold")
print(f"After gold discount: ${discounted:.2f}")

taxed_price = discounted + calculate_tax(discounted, 0.07)
print(f"After tax: ${taxed_price:.2f}")

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

# Exercise 4
def calculate_tax(price, rate):
    return price * rate


def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price


def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax


orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# Exercise 6
x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # what prints here?
print(double_it()) # what prints here?
print(x)           # has x changed?

#The first print(x) prints 100 because x is a global variable.
#print(double_it()) prints 1998 because the function creates its own local variable x = 999 and doubles it.
#The final print(x) prints 100 again because changing the local variable inside the function does not change the global variable.