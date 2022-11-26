def FlattenList( l ):
    empty = []
    for i in range(0, len(l)):
        if type(l[i]) is list:
            empty += l[i]
        else:
            empty.append(l[i])
    print(empty)
    return empty




if __name__=='__main__':
    r = FlattenList( [1, [2], [3,4,5], [6,7], 8] )
    assert r == [1, 2, 3, 4, 5, 6, 7, 8]