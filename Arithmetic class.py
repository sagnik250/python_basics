class arithmetic:

    pass

class add(arithmetic):

    def evaluate(self, x):
        return self + x


class subtract(arithmetic):

    def evaluate(self, x):
        return self - x


class multiply(arithmetic):

    def evaluate(self, x):
        return self * x


class divide(arithmetic):

    def evaluate(self, x):
        if x == 0 :
            return "Error: division by zero"

        else :
            return self / x


print(add.evaluate(4,5))
print(subtract.evaluate(4,5))
print(multiply.evaluate(4,5))
print(divide.evaluate(4,5))
