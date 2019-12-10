"""
A module that represent cars
Classes
-------
Wheel
Engine
CarConstructor(Wheel, Engine)
Car1(CarConstructor)
Car2(CarConstructor)
NewCar(CarConstructor)
"""


class Wheel:
    """
    Class that contain wheels for different cars

    Methods
    -------
    car1_wheels()
    car2_wheels()
    """
    @staticmethod
    def car1_wheels():
        """Return car1 type of the wheels"""
        return 'Continental'

    @staticmethod
    def car2_wheels():
        """Return car2 type of the wheels"""
        return 'Pirelli'


class Engine:
    """
    Class that contain engines for different cars

    Methods
    -------
    car1_engine()
    car2_engine()
    """
    @staticmethod
    def car1_engine():
        """Return car1 engine type"""
        return '1HZ'

    @staticmethod
    def car2_engine():
        """Return car2 engine type"""
        return '1HD-T'


class CarConstructor(Wheel, Engine):
    """
    Construct car blank
    Attributes
    ----------
    wheels
    engine

    Methods
    -------
    get_wheel_type()
    get_engine_type()
    """
    def __init__(self):
        self.wheels = None
        self.engine = None

    def get_wheel_type(self):
        """Return wheel type"""
        return self.wheels

    def get_engine_type(self):
        """Return engine type"""
        return self.engine


class Car1(CarConstructor):
    """Class to create car of a Car1 type"""
    def __init__(self):
        super().__init__()
        self.wheels = self.car1_wheels()
        self.engine = self.car1_engine()


class Car2(CarConstructor):
    """Class to create car of a Car2 type"""
    def __init__(self):
        super().__init__()
        self.wheels = self.car2_wheels()
        self.engine = self.car2_engine()


class NewCar(CarConstructor):
    """Class to create car of a NewCar type"""
    def __init__(self):
        super().__init__()
        self.wheels = self.car1_wheels()
        self.engine = self.car2_engine()
