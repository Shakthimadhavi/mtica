class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.mileage = mileage
    def capacity(self, capacity):
        return f"The seating capacity of a(self.name)\is {capacity} passengers"
class Bus(Vehicle):
    def capacity(self,capacity=50):
        return super().capacity(capacity=50)
school_bus=Bus("school volvo",180,12)
print(school_bus.capacity())
