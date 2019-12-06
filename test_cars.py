import cars


def test_car1():
    c = cars.Car1Builder()
    assert c.get_wheel_type() == 'Continental'
    assert c.get_engine_type() == '1HZ'


def test_car2():
    c = cars.Car2Builder()
    assert c.get_wheel_type() == 'Pirelli'
    assert c.get_engine_type() == '1HD-T'


def test_newcar():
    c = cars.NewCarBuilder()
    assert c.get_wheel_type() == 'Continental'
    assert c.get_engine_type() == '1HD-T'
