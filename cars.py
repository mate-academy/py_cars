"""Design for new cars"""


class Engine:
    """Engine class"""
    def __init__(self):
        self._engine_type1 = '1HZ'
        self._engine_type2 = '1HD-T'

    def get_engine_type1(self):
        """Get first type of engine"""
        return self._engine_type1

    def get_engine_type2(self):
        """Get second type of engine"""
        return self._engine_type2


class Wheel:
    """Wheel's class"""
    def __init__(self):
        self._wheel_type1 = 'Continental'
        self._wheel_type2 = 'Pirelli'

    def get_wheel_type1(self):
        """Get first type of wheel"""
        return self._wheel_type1

    def get_wheel_type2(self):
        """Get second type of wheel"""
        return self._wheel_type2


class BaseCar:
    """Base class for all cars"""
    def __init__(self):
        self._wheel_type = None
        self._engine_type = None
        self._engines = Engine()
        self._wheels = Wheel()

    def get_wheel_type(self):
        """Get wheel type"""
        return self._wheel_type

    def get_engine_type(self):
        """Get engine type"""
        return self._engine_type


class Car1(BaseCar):
    """Class of car1"""
    def __init__(self):
        super().__init__()
        self._engine_type = self._engines.get_engine_type1()
        self._wheel_type = self._wheels.get_wheel_type1()


class Car2(BaseCar):
    """Class of car2"""
    def __init__(self):
        super().__init__()
        self._engine_type = self._engines.get_engine_type2()
        self._wheel_type = self._wheels.get_wheel_type2()


class NewCar(BaseCar):
    """Class of NewCar"""
    def __init__(self):
        super().__init__()
        self._engine_type = self._engines.get_engine_type2()
        self._wheel_type = self._wheels.get_wheel_type1()
