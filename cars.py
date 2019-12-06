"""
Module defines all cars.
Classes
-------
BaseCar
Car1
Car2
NewCar
"""


class Engine:
    """
    Representing engine class.
    Attributes
    ----------
    Methods
    -------
    get_engine_type_1()
    get_engine_type_2()
    """
    def __init__(self):
        self._engine_type_1 = "1HZ"
        self._engine_type_2 = "1HD-T"

    def get_engine_type_1(self):
        """return engine type 1"""
        return self._engine_type_1

    def get_engine_type_2(self):
        """return engine type 2"""
        return self._engine_type_2


class Wheel:
    """
    Representing wheel class.
    Attributes
    ----------
    Methods
    -------
    get_wheel_type_1()
    get_wheel_type_2()
    """
    def __init__(self):
        self._wheel_type_1 = "Continental"
        self._wheel_type_2 = "Pirelli"

    def get_wheel_type_1(self):
        """return wheel type 1"""
        return self._wheel_type_1

    def get_wheel_type_2(self):
        """return wheel type 2"""
        return self._wheel_type_2

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
        self._engine = Engine()
        self._wheel = Wheel()

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
        self._engine_type = self._engine.get_engine_type_1()
        self._wheel_type = self._wheel.get_wheel_type_1()


class Car2(BaseCar):
    """Representing car2 class"""
    def __init__(self):
        super().__init__()
        self._engine_type = self._engine.get_engine_type_2()
        self._wheel_type = self._wheel.get_wheel_type_2()


class NewCar(BaseCar):
    """Representing new car class"""
    def __init__(self):
        super().__init__()
        self._engine_type = self._engine.get_engine_type_2()
        self._wheel_type = self._wheel.get_wheel_type_1()
