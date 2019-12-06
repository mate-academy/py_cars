"""
There are two cars. It is necessary to design a new car
with wheels from the first, and an engine from the second.
"""


class HasAllCar:
    """
    Parent class Car1, Car2, Newcar
    """
    def __init__(self):
        self.wheel_type = ''
        self.engine_type = ''

    def get_wheel_type(self):
        """Get info about wheels"""
        return self.wheel_type

    def get_engine_type(self):
        """Get info about engines"""
        return self.engine_type


class Car1(HasAllCar):
    """Class Car1 has attributes wheel='Continental', engine='1HZ'"""
    def __init__(self, wheel='Continental', engine='1HZ'):
        super().__init__()
        self.wheel_type = wheel
        self.engine_type = engine


class Car2(HasAllCar):
    """Class Car2 has attributes wheel='Pirelli', engine='1HD-T'"""
    def __init__(self, wheel='Pirelli', engine='1HD-T'):
        super().__init__()
        self.wheel_type = wheel
        self.engine_type = engine


class NewCar(Car1, Car2):
    """Class Newcar has attributes class Car1 wheel_type and class Car2 engine_type"""
    def __init__(self):
        super().__init__()
        self.wheel_type = Car1().wheel_type
        self.engine_type = Car2().engine_type
