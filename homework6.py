# Seda Sedrakyan

# Problem 1
print("---Problem 1---")
from abc import ABC, abstractmethod, abstractproperty


class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):

    def draw(self):
        return 'o'


class Square(Shape):

    def draw(self):
        return 'ՔԱՌԱԿՈՒՍԻ'


class Triangle(Shape):

    def draw(self):
        return 'ԵՌԱՆԿՅՈՒՆ ՀԱՎԱՍԱՐԱՍՐՈՒՆ'


class ShapeFactory:
    
    shapes_ = {
        'circle': Circle, 'square': Square, 'triangle': Triangle,
    }


    def build(self, shape):
        return ShapeFactory.shapes_[shape]()


class Client:

    def draw(self, shape):
        factory = ShapeFactory().build(shape)

        return factory.draw()


client = Client()
print(client.draw('triangle'))





# Problem 2
print("---Problem 2---")
class Button(ABC):

    @abstractmethod
    def press(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Checkbox(ABC):

    @abstractmethod
    def change(self):
        pass


class WinButton(Button):

    def press(self):
        return 'WB pressed'




class MacButton(Button):

    def press(self):
        return 'MB pressed'



class WinCheckbox(Checkbox):

    def change(self):
        return 'WB change'


class MacCheckbox(Checkbox):

    def change(self):
        return 'MB change'


class GUIFactory(ABC):

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class WinFactory(GUIFactory):

    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()


class MacFactory(GUIFactory):

    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


class Application:

    def __init__(self, f):

        self.factory = f

    def createUI(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()



# Problem 3
print("---Problem 3---")
class AbstractBuilder(ABC):

    
    def create_id(self, id):
        pass

    def create_balance(self, balance):
        pass

    def create_rate(self, rate):
        pass


class BankAccount():

    def __init__(self):
        self.attributes = {}

    def add_attribute(self, key, value):
        self.attributes[key] = value

    def summary(self):
        print(self.attributes)


class BankAccountBuilder(AbstractBuilder):

    def __init__(self):
        self.bank_account = BankAccount()

    def create_id(self, id):
        self.bank_account.add_attribute('id', id)

    def create_balance(self, balance):
        self.bank_account.add_attribute('balance', balance)

    def create_rate(self, rate):
        self.bank_account.add_attribute('rate', rate)



builder = BankAccountBuilder()
builder.create_id('101')
builder.create_balance(1000)
builder.create_rate(10)
builder.bank_account.summary()
