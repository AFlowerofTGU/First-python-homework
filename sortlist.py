def SortList(lst, order):

    if order == 'asc':
        b = sorted(lst)
    if order == 'desc':
        b = sorted(lst, reverse=True)
    if order == 'none':
        b = lst
    return b


if __name__ == '__main__':
    lst = [1, 3, 2, 5, 4]
    l = SortList(lst, 'asc')
    print(l)
    l = SortList(lst, 'desc')
    print(l)
    l = SortList(lst, 'none')
    print(l)