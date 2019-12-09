"""This program describes the existing cars features
and designs prototype of the new car based on these features"""


class Car1:
    """This class represents the car with some tyres and engine"""
    def __init__(self):
        """Define the characteristics of Car1 tyres and engine"""
        self.wheel_type = 'Continental'
        self.engine_type = '1HZ'

    def get_wheel_type(self):
        """Provide Car1 tyres type"""
        return self.wheel_type

    def get_engine_type(self):
        """Provide Car1 engine type"""
        return self.engine_type


class Car2:
    """This class represents the car with some tyres and engine too"""
    def __init__(self):
        """Define the characteristics of Car2 tyres and engine"""
        self.wheel_type = 'Pirelli'
        self.engine_type = '1HD-T'

    def get_wheel_type(self):
        """Provide Car2 tyres type"""
        return self.wheel_type

    def get_engine_type(self):
        """Provide Car2 engine type"""
        return self.engine_type


class NewCar:
    """This class represents the prototype of the car
    with merged Car1 and Car2 features"""
    @staticmethod
    def get_wheel_type():
        """Provide the Car1 tyres type"""
        car = Car1()
        return car.get_wheel_type()

    @staticmethod
    def get_engine_type():
        """Provide the Car2 engine type"""
        car = Car2()
        return car.get_engine_type()
