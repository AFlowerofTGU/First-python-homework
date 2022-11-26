def CountHeadsAndLegs(m, n):
    for x in range(1,m):
        y = m - x
        if 2 * x + 4 * y == n:
            return (x,y)

if __name__ == '__main__':
    r = CountHeadsAndLegs(35, 94)
    print(r)
    assert r == (23, 12)