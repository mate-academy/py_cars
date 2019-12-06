"""
Module defines all cars.
Classes
-------
BaseCar
Car1
Car2
NewCar
"""


class BaseCar:
    """
    Representing base car class.
    Attributes
    ----------
    Methods
    -------
    get_wheel_type()
    get_engine_type()
    """
    def __init__(self):
        self._engine_type = None
        self._wheel_type = None

    def get_wheel_type(self):
        """return wheel type"""
        return self._wheel_type

    def get_engine_type(self):
        """return engine type"""
        return self._engine_type


class Car1(BaseCar):
    """Representing car1 class"""
    def __init__(self):
        super().__init__()
        self._engine_type = "1HZ"
        self._wheel_type = "Continental"


class Car2(BaseCar):
    """Representing car2 class"""
    def __init__(self):
        super().__init__()
        self._engine_type = "1HD-T"
        self._wheel_type = "Pirelli"


class NewCar(BaseCar):
    """Representing new car class"""
    def __init__(self):
        super().__init__()
        self._engine_type = Car2().get_engine_type()
        self._wheel_type = Car1().get_wheel_type()
