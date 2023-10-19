import math

# Main function to calculate points from defined rules
def calculate_points(receipt):
    points = 0
    total = float(receipt["total"])

    # A rules list with respective point values
    rules = [
        lambda: rule1(receipt, 1),
        lambda: rule2(total, 50),
        lambda: rule3(total, 25),
        lambda: rule4(receipt, 5),
        lambda: rule5(receipt),
        lambda: rule6(receipt, 6),
        lambda: rule7(receipt, 10),
    ]

    for rule in rules:
        points += rule()
    
    return points

# One point for every alphanumeric character in the retailer name.
def rule1(receipt, point):
    return sum(point for char in receipt["retailer"] if char.isalnum())

# 50 points if the total is a round dollar amount with no cents.
def rule2(total, point):
    return point if total == int(total) else 0

# 25 points if the total is a multiple of 0.25.
def rule3(total, point):
    return point if total % 0.25 == 0 else 0

 # 5 points for every two items on the receipt.
def rule4(receipt, point):
    return point * (len(receipt["items"]) // 2)

# If the trimmed length of the item description is a multiple of 3,
# multiply the price by 0.2 and round up to the nearest integer.
def rule5(receipt):
    total = 0
    for item in receipt["items"]:
        if len(item["shortDescription"].strip()) % 3 == 0:
            total += math.ceil(float(item["price"]) * 0.2)
    return total

# 6 points if the day in the purchase date is odd.
def rule6(receipt, point):
    purchase_date = receipt["purchaseDate"].split("-")
    if int(purchase_date[2]) % 2 == 1:
        return point
    return 0

# 10 points if the time of purchase is after 2:00pm and before 4:00pm.
def rule7(receipt, point):
    purchase_time = receipt["purchaseTime"].split(":")
    if 14 <= int(purchase_time[0]) < 16:
        return point
    return 0