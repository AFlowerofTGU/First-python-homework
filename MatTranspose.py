def MatTranspose(m):
    import numpy
    y = numpy.transpose(m)
    x = y.tolist()
    return x


if __name__ == '__main__':
    r = MatTranspose([[1, 2, 3], [4, 5, 6]])
    print(r)
    assert r == [[1, 4], [2, 5], [3, 6]]