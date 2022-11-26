def ReverseDigits( x ):
   str_n = str(x)
   x = int(str_n[::-1])
   return x


if __name__=='__main__':
    n = ReverseDigits( 123 )
    print( n )