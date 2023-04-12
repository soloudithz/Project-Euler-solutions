def fibonacci(count=None, upper_bound=None):
    '''Generate the Fibonacci numbers

    Keyword arguments:
    count -- the max amount of Fibonacci numbers to print
    upper_bound -- the max value to be printed, regardless of count
    '''
    p = pp = 1
    new = 0
    for i in range(count):
        if i in [0, 1]:
            yield 1
        else:
            new = p + pp
            pp, p = p, new
            if new > upper_bound:
                break
            yield new        


fibs = list(fibonacci(count=50, upper_bound=4000000))
even_fibs = []
for i in range(len(fibs)):
    if  (i+1) % 3 == 0:             # every third Fibonacci number is even
        even_fibs.append(fibs[i])
print('The sum of all Fibonacci numbers less than 4000000 is', str(sum(even_fibs)) + '.')
