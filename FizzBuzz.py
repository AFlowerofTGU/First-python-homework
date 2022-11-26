def FizzBuzz(n):
    empty=[]
    for i in range(1, n + 1):
        if i % 4 == 0 and i % 6 == 0:
            empty.append('FizzBuzz')

        elif i % 4 == 0:
            empty.append('Fizz')

        elif i % 6 == 0:
            empty.append('Buzz')

        else:
            empty.append(i)

    return empty

if __name__ == '__main__':
    x = FizzBuzz(13)
    print(x)