# Iterator is object that has a countable number of things.
# Objects can be traversed over using iter() method.
# next() method can also be used for traversing, but we have to pass it some object like;
# numbers = AnyClass(), then next(numbers), examples are given in this code

class Count:  # Class defined
    def __init__(self, start = 1):  # A Durand function defined with initial value of 1, it's usually a Constructor.
        self.num = start

    def __iter__(self):  # Durand function for iteration of numbers or objects.
        return self

    def __next__(self):  # Durand function for iteration.
        num = self.num
        self.num += 1
        return num


number_obj = Count() # Creating instance for Count Class
next(number_obj)  # Passing numbers object to next for iteration
print(next(number_obj)) # 1st Call: It has 1 value it will iterate to value 2 on this call
print(next(number_obj)) # 2nd Call: Value 2 will be iterated to Value 3
print(next(number_obj)) # 3rd Call: Value 3 will be iterated to Value 4
print(next(number_obj)) # 4th Call: Value 4 will be iterated to Value 5
print(next(number_obj)) # 5th Call: Value 5 will be iterated to Value 6

# Each time the next() method is called it will iterate from previous value to next value.