import cars


def test_car1():
    c = cars.Car1()
    assert c.get_wheels() == 'Continental'
    assert c.get_engine() == '1HZ'


def test_car2():
    c = cars.Car2()
    assert c.get_wheels() == 'Pirelli'
    assert c.get_engine() == '1HD-T'


def test_newcar():
    c = cars.NewCar()
    assert c.get_wheels() == 'Continental'
    assert c.get_engine() == '1HD-T'
