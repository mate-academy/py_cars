"""Cars"""


class Engine:
    """Class to represent engines"""
    def __init__(self):
        self._engine_1hz = "1HZ"
        self._engine_1hdt = "1HD-T"

    def get_engine_1hz(self):
        """
        :return: 1HZ engine type
        """
        return self._engine_1hz

    def get_engine_1hdt(self):
        """
        :return: 1HD-T engine type
        """
        return self._engine_1hdt


class Wheels:
    """Class to represent wheels"""
    def __init__(self):
        self._wheels_pirelli = "Pirelli"
        self._wheels_continental = "Continental"

    def get_wheels_pirelli(self):
        """
        :return: pirelli wheels type
        """
        return self._wheels_pirelli

    def get_wheels_continental(self):
        """
        :return: continental wheels type
        """
        return self._wheels_continental


class Car:
    """Class to represent base car"""
    def __init__(self):
        self._wheels = Wheels()
        self._engine = Engine()

    def get_wheels(self):
        """
        :return: wheels type
        """
        return self._wheels

    def get_engine(self):
        """
        :return: engine type
        """
        return self._engine


class Car1(Car):
    """Class to represent car of model 1"""
    def __init__(self):
        super().__init__()
        self._wheels = self._wheels.get_wheels_continental()
        self._engine = self._engine.get_engine_1hz()


class Car2(Car):
    """Class to represent car of model 2"""
    def __init__(self):
        super().__init__()
        self._wheels = self._wheels.get_wheels_pirelli()
        self._engine = self._engine.get_engine_1hdt()


class NewCar(Car):
    """Class to represent new model of car"""
    def __init__(self):
        super().__init__()
        self._wheels = self._wheels.get_wheels_continental()
        self._engine = self._engine.get_engine_1hdt()
