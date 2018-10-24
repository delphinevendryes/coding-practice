
'''
Given a 2-D array where lines and columns are ordered, find an element.
'''


def recSearch(matrix, a, top, bottom, left, right):
    if (top > bottom) | (left > right):
        return False

    if matrix[bottom][right] < a:
        return False

    r = right
    b = bottom

    while (b >= top) & (r >= left):
        if matrix[b][r] == a:
            return True

        if (b == top) & (r == bottom):
            return False

        if matrix[b][r] <= a:
            break

        if b == top:
            r += -1
        if r == left:
            b += -1
        else:
            b += -1
            r += -1

    tr = recSearch(matrix, a, top, b, r, right)
    bl = recSearch(matrix, a, b+1, bottom, left, r)
    return bl | tr


def search(m, a):
    return recSearch(m, a, 0, len(m)-1, 0, len(m[0])-1)

def test():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [11, 12, 13]]
    assert search(m, 17) == False
    assert search(m, 7) == True
    assert search(m, 1) == True
    assert search(m, 11) == True

test()

