"""modules"""


class CarMethodsMixin:
    """class with methods for Cars"""
    def get_engine(self):
        """
        :return: engine type
        """
        return self.engine

    def get_wheels(self):
        """
        :return: wheel type
        """
        return self.wheels


class Car1(CarMethodsMixin):
    """class to represent car with 1HZ engine and continental wheels"""
    def __init__(self):
        self.engine = "1HZ"
        self.wheels = "Continental"


class Car2(CarMethodsMixin):
    """class to represent car with 1HZ engine and continental wheels"""

    def __init__(self):
        self.engine = "1HD-T"
        self.wheels = "Pirelli"


class NewCar(Car1, Car2, CarMethodsMixin):
    """Class to represent a NewCar on base of Car1 and Car2"""
    def __init__(self):
        super().__init__()
        self.wheels = Car1().wheels
        self.engine = Car2().engine
