#from test_arithmetic import arithmetic
class arithmetic:
    def __init__(self, x, y):
        #x and y are the operands to an arithmetic class of operation
        self.x = x
        self.y = y

class add(arithmetic):

    def __init__(self, x, y):
        #Import the 'operand' attribute of the arithmetic class
        #into add class.
        super().__init__(x, y)

    def calculate_result(self):
        return self.x + self.y

    def get_result(self):
        print(calculate_result(self))


add_operation = add(3,4)

print(add_operation.get_result())