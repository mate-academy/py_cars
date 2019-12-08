"""Design for new cars"""


class Car1:
    """Class of car1"""
    def __init__(self):
        self.wheel_type = 'Continental'
        self.engine_type = '1HZ'

    def get_wheel_type(self):
        """Get wheel type"""
        return self.wheel_type

    def get_engine_type(self):
        """Get engine type"""
        return self.engine_type


class Car2(Car1):
    """Class of car2"""
    def __init__(self):
        super().__init__()
        self.wheel_type = 'Pirelli'
        self.engine_type = '1HD-T'


class NewCar(Car2):
    """Class of new car"""
    def __init__(self):
        super().__init__()
        self.wheel_type = 'Continental'
