[code]
'''
Problem 16

'''
In [1]: %timeit sum([int(n) for n in str(2**1000)])
10000 loops, best of 3: 143 �s per loop

In [2]: %timeit sum(map(int, str(2**1000)))
10000 loops, best of 3: 123 �s per loop

[/code]
