
# Create a list of integers from 1 to 20
numbers = list(range(1, 21))

# Use a for loop to find all numbers divisible by 3
divisible_by_3 = []
for num in numbers:
    if num % 3 == 0:
        divisible_by_3.append(num)

# Print the numbers divisible by 3
print("Numbers divisible by 3:", divisible_by_3)