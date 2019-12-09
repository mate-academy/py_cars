"""
Built Car1,Car2,NewCar objects
using pattern Builder
"""


class Wheel:
    """
    wheel types
    """
    def __init__(self):
        """
        defining wheel types
        """
        self._wheel_type_1 = 'Continental'
        self._wheel_type_2 = 'Pirelli'

    def get_wheel_type_1(self):
        """
        return wheel type 1
        :return:
        """
        return self._wheel_type_1

    def get_wheel_type_2(self):
        """
        return wheel type 2
        :return:
        """
        return self._wheel_type_2


class Engine:
    """
    engine types
    """
    def __init__(self):
        """
        defining engine types
        """
        self._engine_type_1 = '1HZ'
        self._engine_type_2 = '1HD-T'

    def get_engine_type_1(self):
        """
        return engine type 1
        :return:
        """
        return self._engine_type_1

    def get_engine_type_2(self):
        """
        return engine type 2
        :return:
        """
        return self._engine_type_2


class CarBlueprint:
    """
    how to build a Car
    """
    def __init__(self):
        self._wheel_type = None
        self._engine_type = None
        self._wheel = Wheel()
        self._engine = Engine()

    def get_wheel_type(self):
        """
        Return wheel type
        :return:
        """
        return self._wheel_type

    def get_engine_type(self):
        """
        Return engine type
        :return:
        """
        return self._engine_type


class Car1(CarBlueprint):
    """
    Model Car1 object
    """
    def __init__(self):
        super().__init__()
        self._wheel_type = self._wheel.get_wheel_type_1()
        self._engine_type = self._engine.get_engine_type_1()


class Car2(CarBlueprint):
    """
    Model Car2 object
    """
    def __init__(self):
        super().__init__()
        self._wheel_type = self._wheel.get_wheel_type_2()
        self._engine_type = self._engine.get_engine_type_2()


class NewCar(CarBlueprint):
    """
    Combined model NewCar object
    """
    def __init__(self):
        super().__init__()
        self._wheel_type = self._wheel.get_wheel_type_1()
        self._engine_type = self._engine.get_engine_type_2()
