# Tạo ra một lớp con Bus, kế thừa lớp Vehicle.
# Chi phí cho mỗi ghế là 150. Tổng chi phí thuê (total fare) bằng sức chứa * 100.
# Nếu là xe Bus nhanh thì cộng thêm phí 10% / chỗ ngồi.
# Tổng số tiền thuê xe là = Total fare + 10% of the total fare.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def giaThueXe(self):
        return self.capacity * 150

class Bus(Vehicle):
    def giaThueXe(self):
        amount = super().giaThueXe()
        amount += amount * 0.1
        return amount

School_bus = Bus("School Volvo", 12, 50)
print("Số tiền thuê xe : ", School_bus.giaThueXe())