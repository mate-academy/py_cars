"""There are two cars. It is necessary to design a new car with wheels
from the first, and an engine from the second."""


class Car1:
    """Class Car1 representation"""

    def __init__(self):
        self.wheel = 'Continental'
        self.engine = '1HZ'

    def get_wheel_type(self):
        """Returns wheel type of Car1"""
        return self.wheel

    def get_engine_type(self):
        """Returns engine type of Car1"""
        return self.engine


class Car2:
    """Class Car1 representation"""

    def __init__(self):
        self.wheel = 'Pirelli'
        self.engine = '1HD-T'

    def get_wheel_type(self):
        """Returns wheel type of Car2"""
        return self.wheel

    def get_engine_type(self):
        """Returns engine type of Car2"""
        return self.engine


class NewCar(Car2, Car1):
    """New Car class representation"""
    def __init__(self):
        super().__init__()
        self.wheel = Car1().wheel
