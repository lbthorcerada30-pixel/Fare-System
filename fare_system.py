# CS3 Pair Assessment: Fare System
# Authors: Lady Bielle T. Horcerada, Rhoujan Jay P. Trinidad, Alexa Johanna E. Barraca
# Section: 9-Sodium

from abc import ABC, abstractmethod
class Vehicle(ABC):
    """Abstract base class for every public vehicle."""
    def __init__(self, plate_number, capacity):
        self.__plate_number = plate_number
        self.__capacity = capacity
    def get_plate_number(self):
        return self.__plate_number
    def set_plate_number(self, plate_number):
        self.__plate_number = plate_number
    # TODO (Part 2): write get_capacity() and set_capacity(capacity).
    # set_capacity only accepts a whole number greater than 0.
    # Otherwise, print "Invalid capacity." and keep the old value.
    @abstractmethod
    def compute_fare(self, distance_km):
        pass
    @abstractmethod
    def describe(self):
        pass
# ===== Jeepney class (Developer A) =====
class Jeepney(Vehicle):
    def __init__(self, plate_number, capacity, route):
        super().__init__(plate_number, capacity)
        self.__route = route

    def get_route(self):
        return self.__route

    def set_route(self, route):
        self.__route = route

    def compute_fare(self, distance_km):
        if distance_km <= 4:
            fare = 13.00
        else:
            fare = 13.00 + (distance_km - 4) * 1.80
        return round(fare, 2)

    def describe(self):
        return f"Jeepney {self.get_plate_number()} | Route: {self.get_route()} | Seats: {self.get_capacity()}"
# ===== Tricycle class (Developer B) =====
class Tricycle(Vehicle):
    def __init__(self, plate_number, capacity, barangay):
        super().__init__(plate_number, capacity)
        self.__barangay = barangay

    def get_barangay(self):
        return self.__barangay

    def set_barangay(self, barangay):
        self.__barangay = barangay

    def compute_fare(self, distance_km):
        if distance_km <= 2:
            fare = 20.00
        else:
            fare = 20.00 + (distance_km - 2) * 5.00
        return round(fare, 2)

    def describe(self):
        return f"Tricycle {self.get_plate_number()} | Barangay: {self.get_barangay()} | Seats: {self.get_capacity()}"

# ===== Test code (Part 6 only) =====