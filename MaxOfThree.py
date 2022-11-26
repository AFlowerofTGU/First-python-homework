def MaxOfThree(x, y, z):
    m = max(x, y, z)
    return m


if __name__ == '__main__':
    m = MaxOfThree(1, 5, 3)
    print(m)
    assert m == 5