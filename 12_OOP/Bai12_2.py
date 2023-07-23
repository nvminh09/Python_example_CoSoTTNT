class Vehicle:
    color = "Trắng"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("Volvo", 180, 12)
print(School_bus.color, School_bus.name, ", Vận tốc : ", School_bus.max_speed, ", quãng đường đã chạy :", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, ", Vận tốc : ", car.max_speed, ", quãng đường đã chạy :", car.mileage)