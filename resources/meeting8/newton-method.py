
def sqrt(x, epsilon = 0.00001):
    """Newton's Method to find square root
       with precision epsilon (Heron's algorithm)"""
    ans = 1
    num_guesses = 0
    while abs(x/ans - ans) > epsilon:
        ans = (x/ans + ans)/2
        num_guesses += 1
    return ans

x = float(input("enter a number: "))

print(sqrt(x))
