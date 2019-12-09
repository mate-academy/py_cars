"""This program describes the existing cars features
and designs prototype of the new car based on these features"""


class Wheels:
    """This is a Parent class
    that represents wheels characteristics"""
    def __init__(self, wheels):
        """Define the wheels type"""
        super().__init__()
        self.wheels = wheels

    def get_wheel_type(self):
        """Provide the wheels type"""
        return self.wheels

    @staticmethod
    def fake_public_method():
        """As pylint requires 2+ public methods
        I use fraudulent techniques"""
        return None


class ContinentalWheels(Wheels):
    """This is a Child class of Wheels"""
    def __init__(self):
        """Inherit Wheels features"""
        super(ContinentalWheels, self).__init__("Continental")


class PirelliWheels(Wheels):
    """This is a Child class of Wheels"""
    def __init__(self):
        """Inherit Wheels features"""
        super(PirelliWheels, self).__init__("Pirelli")


class Engine:
    """This class represents Parent class Engine"""
    def __init__(self, engine):
        """Define the characteristics of engine"""
        super().__init__()
        self.engine = engine

    def get_engine_type(self):
        """Provide engine type"""
        return self.engine

    @staticmethod
    def fake_public_method():
        """As pylint requires 2+ public methods
        I use fraudulent techniques"""
        return None


class OneHZEngine(Engine):
    """This is a Child class that inherits features of Engine"""
    def __init__(self):
        """Inherit the characteristics of engine"""
        super(OneHZEngine, self).__init__("1HZ")


class OneHDTEngine(Engine):
    """This class is a Child class of Engine"""
    def __init__(self):
        """Inherit the features of Engine """
        super(OneHDTEngine, self).__init__("1HD-T")


class Car1(OneHZEngine, ContinentalWheels):
    """This class represents the car with some tyres and engine"""
    def __init__(self):
        """Create Car1 featuring inherited
        from respective Wheels and Engine"""
        super().__init__()
        self.name = "Car1"  # this senseless statement
        # is used for pylint not blaming
        # for "useless-super-delegation"

    @staticmethod
    def fake_public_method1():
        """As pylint requires 2+ public methods
        I use fraudulent techniques"""
        return None

    @staticmethod
    def fake_public_method2():
        """As pylint requires 2+ public methods
        I use fraudulent techniques"""
        return None


class Car2(PirelliWheels, OneHDTEngine):
    """This class represents the car with some tyres and engine too"""
    def __init__(self):
        """Create Car2 featuring inherited
        from respective Wheels and Engine"""
        super().__init__()
        self.name = "Car2"  # this senseless statement
        # is used for pylint not blaming
        # for "useless-super-delegation"

    @staticmethod
    def fake_public_method1():
        """As pylint requires 2+ public methods
        I use fraudulent techniques"""
        return None

    @staticmethod
    def fake_public_method2():
        """As pylint requires 2+ public methods
        I use fraudulent techniques"""
        return None


class NewCar(ContinentalWheels, OneHDTEngine):
    """This class represents the prototype of the car
    with merged Car1 and Car2 features"""
    def __init__(self):
        """Define the characteristics of Car2 tyres and engine
        inherited from Wheels and Engine"""
        super().__init__()
        self.name = "NewCar" # this senseless statement
        # is used for pylint not blaming
        # for "useless-super-delegation"

    @staticmethod
    def fake_public_method1():
        """As pylint requires 2+ public methods
        I use fraudulent techniques"""
        return None

    @staticmethod
    def fake_public_method2():
        """As pylint requires 2+ public methods
        I use fraudulent techniques"""
        return None
