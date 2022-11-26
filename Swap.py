def Swap(a, b):
    c = 0
    c = a
    a = b
    b = c
    return a,b
if __name__ == '__main__':
    x, y = Swap(3., 5)
    print(x, y)