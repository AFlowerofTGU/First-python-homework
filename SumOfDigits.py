def SumOfDigits( n ):
    sum = 0
    while n % 10 != 0:
        a = n % 10
        n = n // 10
        sum += a
        return sum

if __name__=='__main__':
    s = SumOfDigits( 12345 )
    print( s )