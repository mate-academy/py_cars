"""modules"""


class CarMethodsMixin:
    """class with methods for Cars"""
    def get_engine_type(self):
        """
        :return: engine type
        """
        return self.engine_type

    def get_wheel_type(self):
        """
        :return: wheel type
        """
        return self.wheel_type


class Car1(CarMethodsMixin):
    """class to represent car with 1HZ engine and continental wheels"""
    def __init__(self):
        self.engine_type = "1HZ"
        self.wheel_type = "Continental"


class Car2(CarMethodsMixin):
    """class to represent car with 1HZ engine and continental wheels"""

    def __init__(self):
        self.engine_type = "1HD-T"
        self.wheel_type = "Pirelli"


class NewCar(Car1, Car2, CarMethodsMixin):
    """Class to represent a NewCar on base of Car1 and Car2"""
    def __init__(self):
        super().__init__()
        self.wheels_type = Car1().wheel_type
        self.engine_type = Car2().engine_type
