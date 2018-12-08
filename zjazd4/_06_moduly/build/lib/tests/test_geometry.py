from _06_moduly.mathematica.geometry import figures


def test_square_area():
    assert figures.square_area(a=5) == 25


def test_triangle_area():
    assert figures.triangle_area(a=5, h=3) == 7.5
