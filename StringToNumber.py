def StringToNumber(s):
    if s.isdigit():
        s = int(s)
    else:
        s = float(s)
    return s

if __name__=='__main__':
    x = StringToNumber( '12345.123' )
    print( x )
