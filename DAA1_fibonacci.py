def fibonacci_iterative(n: int):
    if n <= 0:
        return "Invalid input! Enter n >= 1"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        dp = [0] * n
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]


def fibonacci_recursive(n: int):
    if n <= 0:
        return "Invalid input! Enter n >= 1"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


n = int(input("Enter value of n (nth Fibonacci number): "))

print(f"Fibonacci Number (Iterative): {fibonacci_iterative(n)}")
print(f"Fibonacci Number (Recursive): {fibonacci_recursive(n)}")

print("\nFibonacci Series (Iterative): ", end="") #O(n) time and O(n) space
for i in range(1, n + 1):
    print(fibonacci_iterative(i), end=" ")

print("\nFibonacci Series (Recursive): ", end="") #O(2^n) time and O(n) space
for i in range(1, n + 1):
    print(fibonacci_recursive(i), end=" ")
