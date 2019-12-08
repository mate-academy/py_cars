"""There are two cars. It is necessary to design a new car
with wheels from the first, and an engine from the second."""


class Car:
    """Car object. Return wheel and engine type"""
    def __init__(self):
        self. wheel_type = None
        self. engine_type = None

    def get_wheel_type(self):
        """return wheel type"""
        return self.wheel_type

    def get_engine_type(self):
        """return engine type"""
        return self.engine_type

    def __repr__(self):
        return f"{self.get_engine_type()},{self.get_wheel_type()}"


class Car1(Car):
    """First car. Wheel: Continental. Engine: 1HZ"""
    def __init__(self):
        super().__init__()
        self.wheel_type = "Continental"
        self.engine_type = "1HZ"


class Car2(Car):
    """Second car: Wheel: Pirelli. Engine: 1HD-T"""
    def __init__(self):
        super().__init__()
        self.wheel_type = "Pirelli"
        self.engine_type = "1HD-T"


class NewCar(Car1, Car2):
    """The new car. Wheels from the firs (Continental),
    engine from the second (1HD-T)"""
    def __init__(self):
        super().__init__()
        self.wheel_type = Car1().get_wheel_type()
        self.engine_type = Car2().get_engine_type()

