def SumOfItems(l):
    sum = 0
    for i in range(len(l)):
        sum += int(l[i])
    return sum

if __name__ == '__main__':
    r = SumOfItems([1, '234', '456', 670., '91000'])
    print(r)
    assert r == 92361.

