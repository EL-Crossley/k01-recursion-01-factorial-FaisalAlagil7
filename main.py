# Put your function here
def factorial(n):
    x = int(n)
    if (x < 1):
        return "Zero or negative numbers are not valid"
    if x == 1:
        return n
    elif (x > 1):
        return x * factorial(x-1)

# testing
num = input("")
print(factorial(num))