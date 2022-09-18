def operate(n1, n2, operator):
    if operator == '+':
        return n1 + n2
    if operator == '-':
        return n1 - n2
    if operator == '*':
        return n1 * n2
    if operator == '/':
        return n1 / n2

class Calculator:
    operators = ['+', '-', '*', '/']

    def __init__(self):
        self.current_number = 0
        self.current_operator = None
        self.memory = None
        self.last_input = None
    
    def press_digit(self, digit):
        assert(type(digit) is int)
        assert(0 <= digit <= 9)
        if self.last_input is None or type(self.last_input) is int:
            self.current_number = int(str(self.current_number) + str(digit))
        elif type(self.last_input) is str:
            self.memory = self.current_number
            self.current_number = digit
        self.last_input = digit
    
    def press_operator(self, operator):
        assert(operator in self.operators)
        if self.memory is not None:
            self.current_number = operate(self.memory, self.current_number, self.current_operator)
        self.current_operator = operator
        self.last_input = operator
    
    def press_equal(self):
        if self.memory is not None:
            self.current_number = operate(self.memory, self.current_number, self.current_operator)
        self.last_input = None
    
    def press_clear(self):
        self.current_number = 0
        self.current_operator = None
        self.memory = None
        self.last_input = None
