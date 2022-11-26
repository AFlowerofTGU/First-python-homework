def IsLeapYear(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        y= True
    else:
        y = False
    return y

if __name__ == '__main__':
    r = IsLeapYear(2021)
    print(r)
    assert r == True