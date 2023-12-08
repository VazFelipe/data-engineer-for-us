from bank import value

def test_0():
    assert value("hello") == 0
    assert value("Hello") == 0

def test_20():
    assert value("hi") == 20
    assert value("Hi") == 20

def test_100():
    assert value("OMG") == 100
    assert value("1") == 100

def test_nothing():
    assert value("") == 100

def test_case_insensitivity():
    assert value("OmG") == 100

