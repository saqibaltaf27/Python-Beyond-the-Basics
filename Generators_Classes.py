# ADVANTAGES OF USING GENERATORS:
# 1. Easy to implement.
# 2. Memory Efficient(requires less memory).
# 3. Represent infinite stream.
# 4. Pipelining Generators.

class Generator:
    @staticmethod
    def count():
        for i in range(10):
            yield i+1


object_class = Generator()
next(object_class.count())
print("Using Classes : ", next(object_class.count()))

# This upper function can be written as;
count = (i+1 for i in range(10))
next(count)
print("Using Generators : ", next(count))
