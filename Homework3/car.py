class Car:
    def __init__(self, model, color, max_speed):
        self.model = model
        self.color = color
        self.max_speed = max_speed

    def compareCar(self, car2):
        if self.max_speed > car2.max_speed:
            print("car1 is better than car2")
        else:
            print("car2 is better than car1")

car_1 = Car("Lexus RX", "Black", "350")
car_2 = Car("Sequoia 200", "White", "300")

car_1.compareCar(car_2)
