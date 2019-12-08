"""
Cars objects construction
"""


class Car:
    """
    general Car class
    """
    def __init__(self, wheel, engine):
        """

        :param wheel:
        :param engine:
        """
        self.wheel = wheel
        self.engine = engine

    def get_wheel_type(self):
        """
        return wheel model
        :return:
        """
        return f"{self.wheel}"

    def get_engine_type(self):
        """
        return engine model
        :return:
        """
        return f"{self.engine}"


class Car1(Car):
    """
    instance of the Car object
    with parts of type 1
    """
    def __init__(self):
        """
        setting parts model's of Car type 1
        """
        super().__init__(wheel='Continental', engine='1HZ')


class Car2(Car):
    """
    instance of the Car object
    with parts of type 2
    """
    def __init__(self):
        """
        setting parts model's of Car type 2
        """
        super().__init__(wheel='Pirelli', engine='1HD-T')


class NewCar(Car):
    """
    instance of the Car object
    with combined parts of type 1 and 2
    """
    def __init__(self):
        """
        setting parts model's combined of two types
        """
        super().__init__(wheel=Car1().wheel, engine=Car2().engine)
