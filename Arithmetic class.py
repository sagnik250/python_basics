class arithmetic:

    def __add__(self, x, y) :
        return x + y

    def __sub__(self, x, y):
        return x - y

    def __mul__(self, x, y):
        return x * y

    def __div__(self, x, y):
        return x / y

    def __pow__(self, x, y):
        return x ** y


operation = arithmetic()
print(operation.__add__(3,4))
print(operation.__sub__(6,1))
print(operation.__mul__(24,7))
print(operation.__div__(55,11))
print(operation.__pow__(6,4))