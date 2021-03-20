class Calculation:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def addition(self):
        return self.x + self.y
    
    def subtraction(self):
        return self.x - self.y
    
class MyCalculation(Calculation):
    
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def multiplication(self):
        return self.x * self.y
    
    def division(self):
        return self.x/self.y

test = MyCalculation(10, 1000)
print(test.addition())
print(test.subtraction())
print(test.multiplication())
print(test.division())