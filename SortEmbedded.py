def CompareItems(item):
    for i in range(0,len(item)):
        if type(item[i]) is list:
           item[i].sort()
    return item

def SortEmbedded(l):
    l= CompareItems(l)  # l=(1,[12,13],[5,6,7,8,9])
    empty = []
    list1 = []
    b = 0
    for i in range(0,len(l)):
        if type(l[i]) is list:
            empty.append(l[i][0])
        else:
            empty.append(l[i])
    empty.sort()  # empty = [1,12,5]   ->[1,5,12]
    for i in range(0,len(empty)):
        for j in range(0,len(l)):
            if type(l[j]) is list:
                if l[j][0]==empty[i]:
                   list1.append(l[j])
            else:
                if l[j]==empty[i]:
                    list1.append(l[j])
    return list1

if __name__ == '__main__':
    r = SortEmbedded([1, [13, 12], [6, 5, 7, 8, 9]])

    print(r)
    # assert r == [1, [5, 6, 7, 8, 9], [12, 13]]