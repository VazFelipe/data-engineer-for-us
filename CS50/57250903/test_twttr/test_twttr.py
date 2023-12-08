from twttr import shorten

def test_uppercase():
    assert shorten("CS50") == "CS50"
    assert shorten("ABIOU") == "B"

def test_lowercase():
    assert shorten("cs50") == "cs50"
    assert shorten("abiou") == "b"

def test_vowels():
    assert shorten("aeiou") == ""
    assert shorten("aBiou") == "B"
    assert shorten("What's your name?") == "Wht's yr nm?"
