"""
There are two cars. It is necessary to design a new car
with wheels from the first, and an engine from the second.
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
    Represents car elements
    """

    def __init__(self):
        self.__wheel_type = None
        self.__engine_type = None

    def set_wheel_type(self, wheel):
        """
        Set wheel type for car
        :param wheel: str
        :return: str
        """
        self.__wheel_type.append(wheel)

    def set_engine_type(self, engine):
        """
        Set engine type for car
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
        :return:
        """

    def get_engine_type(self):
        """
        Return engine type of the car2.
        :return:
        """


class Car1Builder(Builder):
    """
    Child class is responsible for creating car1 type
    inheritance from parent Builder class.
    """

    def get_wheel_type(self):
        """
        Return wheel type of the car1.
        :return: str
        """
        wheel = Wheel()
        wheel.type = 'Continental'
        return wheel.type

    def get_engine_type(self):
        """
        Return engine type of the car1.
        :return: str
        """
        engine = Engine()
        engine.type = '1HZ'
        return engine.type


class Car2Builder(Builder):
    """
    Child class is responsible for creating car2 type
    inheritance from parent Builder class.
    """

    def get_wheel_type(self):
        """
        Return wheel type of the car2.
        :return: str
        """
        wheel = Wheel()
        wheel.type = 'Pirelli'
        return wheel.type

    def get_engine_type(self):
        """
        Return engine type of the car2.
        :return: str
        """
        engine = Engine()
        engine.type = '1HD-T'
        return engine.type


class NewCarBuilder(Builder):
    """
    Child class is responsible for creating new car type
    that consists from car1 wheel type and car2 engine type
    inheritance from parent Builder class.
    """

    def get_wheel_type(self):
        """
        Return wheel type of the new car.
        :return: str
        """
        wheel = Wheel()
        car1 = Car1Builder()
        wheel.type = car1.get_wheel_type()
        return wheel.type

    def get_engine_type(self):
        """
        Return engine type of the new car.
        :return: str
        """
        engine = Engine()
        car2 = Car2Builder()
        engine.type = car2.get_engine_type()
        return engine.type
