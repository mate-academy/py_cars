"""
tests
"""
import cars


def test_car1():
    """
    testing Car1 parts
    :return:
    """
    c = cars.Car1()
    assert c.get_wheel_type() == 'Continental'
    assert c.get_engine_type() == '1HZ'


def test_car2():
    """
    testing Car2 parts
    :return:
    """
    c = cars.Car2()
    assert c.get_wheel_type() == 'Pirelli'
    assert c.get_engine_type() == '1HD-T'


def test_new_car():
    """
    testing NewCar parts
    :return:
    """
    c = cars.NewCar()
    assert c.get_wheel_type() == 'Continental'
    assert c.get_engine_type() == '1HD-T'
