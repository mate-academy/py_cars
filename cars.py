"""
Module
"""


class Wheel:
    """
    Wheel class
    """
    type = None

    def __str__(self) -> str:
        return f"Wheel({self.type})"

    def __repr__(self) -> str:
        return f"W<({self.type})>"


class Engine:
    """
    Engine class
    """
    type = None

    def __str__(self) -> str:
        return f"Engine({self.type})"

    def __repr__(self) -> str:
        return f"E<({self.type})>"


class Car:
    """
    Represents car
    """

    def __init__(self):
        self.__wheel_type = None
        self.__engine_type = None

    def set_wheel_type(self, wheel):
        """
        :param wheel: str
        :return: str
        """
        self.__wheel_type = wheel

    def set_engine_type(self, engine):
        """
        :param wheel: str
        :return: str
        """
        self.__engine_type = engine


class Builder:
    """
    Class is responsible for constructing varieties of cars.
    """

    def get_wheel_type(self):
        """
        Return wheel type of the car.
        """

    def get_engine_type(self):
        """
        Return engine type of the car.
        """


class Car1(Builder):
    """
    Class for car1
    """

    def get_wheel_type(self):
        """
        :return: str
        """
        wheel = Wheel()
        wheel.type = 'Continental'
        return wheel.type

    def get_engine_type(self):
        """
        :return: str
        """
        engine = Engine()
        engine.type = '1HZ'
        return engine.type


class Car2(Builder):
    """
    Class for car2
    """

    def get_wheel_type(self):
        """
        :return: str
        """
        wheel = Wheel()
        wheel.type = 'Pirelli'
        return wheel.type

    def get_engine_type(self):
        """
        :return: str
        """
        engine = Engine()
        engine.type = '1HD-T'
        return engine.type


class NewCar(Builder):
    """
    Class for newcar
    """

    def get_wheel_type(self):
        """
        :return: str
        """
        wheel = Wheel()
        car1 = Car1()
        wheel.type = car1.get_wheel_type()
        return wheel.type

    def get_engine_type(self):
        """
        :return: str
        """
        engine = Engine()
        car2 = Car2()
        engine.type = car2.get_engine_type()
        return engine.type
