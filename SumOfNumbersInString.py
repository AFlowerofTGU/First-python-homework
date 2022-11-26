def SumOfNumbersInString(s):
    sum  = 0
    a = s.split(" ")
    for i in range(len(a)):
        if a[i].isnumeric():
            sum += int(a[i])

    return sum

if __name__ == '__main__':
    s = '123 abc 45678 defghijk 1'
    t = SumOfNumbersInString(s)
    print(t)
    assert t == 123 + 45678 + 1