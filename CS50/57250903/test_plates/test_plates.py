from plates import is_valid

def test_two_letters():
    assert is_valid("CS50") == True
    assert is_valid("A4AA") == False

def test_number_middle():
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False

def test_number_char():
    assert is_valid("AAA222") == True
    assert is_valid("CS") == True
    assert is_valid("AAA2222") == False
    assert is_valid("A") == False

def test_punctuation_spaces_periods():
    assert is_valid("CS.50") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS!50") == False

def test_only_number():
    assert is_valid("000000") == False
    assert is_valid("999999") == False


