import random
numbers = [random.randint(1, 100) for _ in range(10)]
odd_numbers =[]
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
print("odd numbers:", odd_numbers)