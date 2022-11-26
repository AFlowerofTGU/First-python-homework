def DecToBin(n):
    if n >= 1:
        DecToBin(n // 2)
    print(n % 2, end='')


if __name__ == '__main__':
    s = DecToBin(32)
    print(s)