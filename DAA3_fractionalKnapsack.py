class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def fractional_knapsack(items, capacity):
    # Calculate value-to-weight ratio for each item
    ratio_list = [(item.value / item.weight, item) for item in items]   # list of (ratio, item)
    ratio_list.sort(reverse=True, key=lambda x: x[0])  # sort by ratio (high → low)

    total_value = 0.0
    knapsack = []

    for ratio, item in ratio_list:
        if capacity == 0:
            break

        # Take as much as possible of the current item
        take_weight = min(item.weight, capacity) # weight to take
        total_value += take_weight * ratio # update total value
        capacity -= take_weight # update remaining capacity

        knapsack.append((item, take_weight, take_weight / item.weight))  # store fraction info

    return total_value, knapsack


# -------- Main Program --------
#while True:
#print("\nPress Ctrl+C to terminate...")
n = int(input("Enter number of items: "))

print("Enter values of items (space separated): ")
values = list(map(float, input().split())) 

print("Enter weights of items (space separated): ")
weights = list(map(float, input().split()))

capacity = float(input("Enter maximum weight capacity: ")) 

# Create item objects
items = [Item(weights[i], values[i]) for i in range(n)] # list of Item objects

# Run fractional knapsack
max_value, selected_items = fractional_knapsack(items, capacity) # get max value and selected items

print("\nSelected Items:")
for item, taken_weight, fraction in selected_items:
    print(f"Item (value={item.value}, weight={item.weight}) -> fraction taken: {fraction:.2f}")

print(f"\nMaximum value achievable: {max_value:.2f}")

#time complexity: O(n log n) due to sorting of items based on value-to-weight ratio
#Space complexity: O(n) for storing item details