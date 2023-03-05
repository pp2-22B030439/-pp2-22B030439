import ast
user_input = input('Enter space-separated integers: ')
my_tuple = tuple(bool(item) for item in user_input.split())
result = all(my_tuple)
print(result)