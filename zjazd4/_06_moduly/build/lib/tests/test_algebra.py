from _06_moduly.mathematica.algebra import matrices


def test_add_matrices():
    a = [[1,2,3],[4,5,6]]
    b = [[0,9,8],[4,5,6]]
    assert matrices.add_matrices(a,b) == [[1,11,11],[8,10,12]]

def test_add_matrices_ver2():
    a = [[1,2,3],[4,5,6]]
    b = [[0,9,8],[4,5,6]]
    assert matrices.add_matrices_ver2(a,b) == [[1,11,11],[8,10,12]]

def test_sub_matrices():
    a = [[1,2,3],[4,5,6]]
    b = [[0,9,8],[4,5,6]]
    assert matrices.sub_matrices(a,b) == [[1,-7,-5],[0,0,0]]

def test_sub_matrices_ver2():
    a = [[1,2,3],[4,5,6]]
    b = [[0,9,8],[4,5,6]]
    assert matrices.sub_matrices_ver2(a,b) == [[1,-7,-5],[0,0,0]]