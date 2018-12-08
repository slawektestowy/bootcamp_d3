# add_matrices i sub_matrices

# [[1,2,3]
# ,[4,5,6]]

def add_matrices(a, b):
    result = []
    for x, row in enumerate(a):
        res_row = []
        for y, el in enumerate(row):
            res_row.append(el + b[x][y])
        result.append(res_row)
    return result


def sub_matrices(a, b):
    result = []
    for x, row in enumerate(a):
        res_row = []
        for y, el in enumerate(row):
            res_row.append(el - b[x][y])
        result.append(res_row)
    return result


def add_matrices_ver2(a, b):
    result = []
    for row_a, row_b in zip(a, b):
        res_row = []
        for el_a, el_b in zip(row_a, row_b):
            res_row.append(el_a + el_b)
        result.append(res_row)
    return result

def sub_matrices_ver2(a, b):
    result = []
    for row_a, row_b in zip(a, b):
        res_row = []
        for el_a, el_b in zip(row_a, row_b):
            res_row.append(el_a - el_b)
        result.append(res_row)
    return result
