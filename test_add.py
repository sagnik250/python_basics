from test_arithmetic import arithmetic

class add(arithmetic):

    def __init__(self, x, y):
        #Import the 'operand' attribute of the arithmetic class
        #into add class.
        super().__init__(x, y)

    def calculate_result(self):
        return self.x + self.y

    def get_result(self):
        print(calculate_result(self))
