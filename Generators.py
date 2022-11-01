# 1. Generators always return iterator objects.
# 2. yield keyword is used.
# 3. called by next() method.
# 4. They are called 'lazy iterators', because they don't store in memory.

# Function for Generator
def get_sequence(x):
    for i in range(x):
        yield i     # yield keyword used in generators

sequence = get_sequence(4)
print(sequence) # It will print Generator Object for us.
# Output: <generator object get_sequence at 0x7f51a06866d0>
print(next(sequence)) # 1st Output = 0
print(next(sequence)) # 2nd Output = 1
print(next(sequence)) # 3rd Output = 2
print(next(sequence)) # 4th Output = 3
print(next(sequence)) # 5th On this iteration it will stop because of range given and will give error
# Output : Traceback (most recent call last): StopIteration