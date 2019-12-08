"""
There are two cars. It is necessary to design a new car
with wheels from the first, and an engine from the second.
"""


class MiximCar:
    """
    Parent class Car1, Car2, NewCar
    """
    wheel = ''
    engine = ''

    @classmethod
    def get_wheel_type(cls):
        """Get info about wheels"""
        return cls.wheel

    @classmethod
    def get_engine_type(cls):
        """Get info about engines"""
        return cls.engine


class Car1(MiximCar):
    """Class Car1 has attributes wheel='Continental', engine='1HZ'"""
    wheel = 'Continental'
    engine = '1HZ'


class Car2(MiximCar):
    """Class Car2 has attributes wheel='Pirelli', engine='1HD-T'"""
    wheel = 'Pirelli'
    engine = '1HD-T'


class NewCar(Car1, Car2):
    """Class Newcar has attributes class Car1 wheel_type and class Car2 engine_type"""
    wheel = Car1.wheel
    engine = Car2.engine
