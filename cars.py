"""
There are two cars. It is necessary to design a new car
with wheels from the first, and an engine from the second.
"""


class Wheel:
    """Class Wheel"""
    def __init__(self):
        super().__init__()
        self.wheels = ['Continental', 'Pirelli']

    def get_wheel_car1(self):
        """Get wheel for car1"""
        return self.wheels[0]

    def get_wheel_car2(self):
        """Get wheel for car2"""
        return self.wheels[1]


class Engine:
    """Class Engine"""
    def __init__(self):
        super().__init__()
        self.engines = ['1HZ', '1HD-T']

    def get_engine_car1(self):
        """Get engine for car1"""
        return self.engines[0]

    def get_engine_car2(self):
        """Get engine for car2"""
        return self.engines[1]


class CarConstructor(Wheel, Engine):
    """Class CarConstructor"""
    def __init__(self):
        super().__init__()
        self.wheel = ''
        self.engine = ''

    def get_wheel_type(self):
        """Get wheel"""
        return self.wheel

    def get_engine_type(self):
        """Get engine"""
        return self.engine


class Car1(CarConstructor):
    """Class Car1"""
    def __init__(self):
        super().__init__()
        self.wheel = self.get_wheel_car1()
        self.engine = self.get_engine_car1()


class Car2(CarConstructor):
    """Class Car2"""
    def __init__(self):
        super().__init__()
        self.wheel = self.get_wheel_car2()
        self.engine = self.get_engine_car2()


class NewCar(CarConstructor):
    """Class NewCar"""
    def __init__(self):
        super().__init__()
        self.wheel = self.get_wheel_car1()
        self.engine = self.get_engine_car2()
