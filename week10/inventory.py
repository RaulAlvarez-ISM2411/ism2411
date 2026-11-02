
# Module 10 Reflection
#1. the most surprising thing about Python lists is how easy it is to change them by adding, removing, or rearranging items. I also learned that negative indexes let me access items starting from the end.
#2. For a class project like WearAbouts, I could use a Python list to keep track of clothing prices and calculate discounts automatically. This would save time compared to entering and calculating every price manually in Excel.

# Exercise 1 
inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print("EXERCISE 1")
print(inventory)
print("Total items:", len(inventory))


# Exercise 2
print("\nEXERCISE 2")
print("First item:", inventory[0])
print("Last item:", inventory[-1])
print("Middle item:", inventory[len(inventory) // 2])


# Exercise 3
print("\nEXERCISE 3")
print("First three:", inventory[:3])
print("Last two:", inventory[-2:])
print("Every other item:", inventory[::2])


# Exercise 4
print("\nEXERCISE 4")
inventory.append("envelope")
print("After appending:", inventory)

inventory.remove("tape")
print("After removing tape:", inventory)

inventory.sort()
print("After sorting:", inventory)


# Exercise 5
print("\nEXERCISE 5")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples cannot be changed, which makes them useful for storing coordinates that should stay the same.")

print("Original coordinates:", coords)


# Exercise 6
print("\nEXERCISE 6")
sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count
best = max(sales)
worst = min(sales)

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", best)
print("Worst:", worst)


# Exercise 7
print("\nEXERCISE 7")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    discounted.append(round(price * 0.90, 2))

print("Original prices:", prices)
print("Discounted prices:", discounted)


# Exercise 8
print("\nEXERCISE 8")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print("High sales:", high_sales)
print("Count:", len(high_sales))
print("Average:", round(sum(high_sales) / len(high_sales), 2))
