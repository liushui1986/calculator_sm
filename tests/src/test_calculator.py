from app.src.calculator import Calculator

cal = Calculator()

def test_app():
    assert cal.add(1, 1) == 2
    assert cal.add(1, 2) == 3
