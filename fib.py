# use generator
# from 
# http://stackoverflow.com/questions/1756096/understanding-generators-in-python
'''
use for loop to test
>>> a = fib()
>>> for i in range(10):
...     print(next(a))
... 
0
1
1
2
3
5
8
13
21
34
>>> import itertools
>>> list(itertools.islice(fib(),10))
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# see fib() can generate an infinite streams like Fibonacci numbers.
if __name__ == '__main__':
    import doctest
    doctest.testmod()
