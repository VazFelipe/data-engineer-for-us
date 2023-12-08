import pytest
from fuel import convert, gauge

def test_percentage():
    assert gauge(convert("2/3")) == "67%"

def test_full():
    assert gauge(convert("1/1")) == "F"

def test_empty():
    assert gauge(convert("0/1")) == "E"

def test_empty():
    assert gauge(convert("1/100")) == "E"

def test_full():
    assert gauge(convert("99/100")) == "F"

def test_zerodivisionerror():
    with pytest.raises(ZeroDivisionError):
        gauge(convert("1/0"))

def test_value_error():
    with pytest.raises(ValueError):
        gauge(convert("2/1"))
