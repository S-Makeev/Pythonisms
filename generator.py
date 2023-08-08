def even_numbers_generator(limit):
    num = 2  # Start with the first even number
    while num <= limit:
        yield num  # Yield the current even number
        num += 2   # Move to the next even number

# Create a generator object
evens = even_numbers_generator(10)

# Iterate through the generated even numbers
for even_num in evens:
    print(even_num)