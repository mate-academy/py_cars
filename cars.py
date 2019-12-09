"""This program describes the existing cars features
and designs prototype of the new car based on these features"""


class Car1:
    """This class represents the car with predetermined tyres and engine"""

    @staticmethod
    def get_wheel_type():
        """Provide Car1 tyres type"""
        return "Continental"

    @staticmethod
    def get_engine_type():
        """Provide Car1 engine type"""
        return "1HZ"


class Car2:
    """This class represents the car with predetermined tyres and engine too"""

    @staticmethod
    def get_wheel_type():
        """Provide Car2 tyres type"""
        return "Pirelli"

    @staticmethod
    def get_engine_type():
        """Provide Car2 engine type"""
        return "1HD-T"


class NewCar:
    """This class represents the prototype of the car
    with merged Car1 and Car2 predetermined features"""
    @staticmethod
    def get_wheel_type():
        """Provide the Car1 tyres type"""
        return Car1.get_wheel_type()

    @staticmethod
    def get_engine_type():
        """Provide the Car2 engine type"""
        return Car2.get_engine_type()
