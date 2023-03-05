def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
a = input().split()
b = list(map(int, a))
print(multiply(b))
