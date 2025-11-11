# ---------------- 0/1 Knapsack using Dynamic Programming (Tabulation + Item Tracking) ----------------

def knapsack(W, val, wt):
    n = len(val)
    # Create DP table (n+1) x (W+1)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build the DP table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                include = val[i - 1] + dp[i - 1][w - wt[i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]

    # Maximum value is stored at dp[n][W]
    max_value = dp[n][W]

    # ---------- TRACEBACK: Find which items were included ----------
    included_items = []
    w = W
    for i in range(n, 0, -1):
        # If the value comes from including the ith item
        if dp[i][w] != dp[i - 1][w]:
            included_items.append(i)  # Store the 1-based index
            w -= wt[i - 1]  # Reduce remaining capacity

    included_items.reverse()  # Reverse to preserve original order
    return max_value, included_items


# ---------- MAIN PROGRAM ----------
print("0/1 Knapsack Problem using Dynamic Programming\n")

# Input number of items
n = int(input("Enter number of items: "))

val = []
wt = []

# Take input item by item
for i in range(n):
    print(f"\nEnter details of item {i + 1}:")
    value = int(input("  Value: "))
    weight = int(input("  Weight: "))
    val.append(value)
    wt.append(weight)

# Input maximum weight capacity
W = int(input("\nEnter maximum weight capacity: "))

# Compute maximum value and included items
max_value, included_items = knapsack(W, val, wt)

print(f"\n✅ Maximum value that can be carried: {max_value}")

if len(val) != n or len(wt) != n:
    print("\n❌ Error: Number of values and weights must match the number of items.")
else:
    # Compute maximum value and included items
    max_value, included_items = knapsack(W, val, wt)

    if included_items:
        print("\nIncluded items:")
        for i in included_items:
            print(f"Item {i}: value = {val[i-1]}, weight = {wt[i-1]}")
    else:
        print("\nNo items were included (possibly all items too heavy).")
#time complexity: O(n*W)
#space complexity: O(n*W)