"""
A module that represent cars
Classes
-------
Car
Car1(Car)
Car2(Car)
NewCar(Car)
"""


class Car:
    """
    Represent general car
    Attributes
    ----------
    wheel_type : str  --  type of the wheels
    engine_type : str -- type of the engine
    Methods
    -------
    get_wheel_type
    get_engine_type
    """
    def __init__(self, wheel_type, engine_type):
        self.wheel_type = wheel_type
        self.engine_type = engine_type

    def get_wheel_type(self):
        """Return wheel type"""
        return self.wheel_type

    def get_engine_type(self):
        """Return engine type"""
        return self.engine_type


class Car1(Car):
    """
    A class to represent a unique car - Car1(Car)
    """
    def __init__(self):
        super().__init__('Continental', '1HZ')


class Car2(Car):
    """
    A class to represent a unique car - Car2(Car)
    """
    def __init__(self):
        super().__init__('Pirelli', '1HD-T')


class NewCar(Car):
    """
    A class to represent a unique car - NewCar(Car)
    """
    def __init__(self):
        super().__init__(Car1().wheel_type, Car2().engine_type)
