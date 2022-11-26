def RemoveDuplicate(l):
    for i in range(len(l) - 1, 0, -1):
        if l[i] == l[i - 1]:
            l.pop(i)

    return l

if __name__ == '__main__':
    l = [0, 0, 1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 2, 2]
    r = RemoveDuplicate(l)
    print(r)
    assert r == [0, 1, 2, 3, 4, 5, 6, 2]