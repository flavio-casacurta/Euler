[code]
'''
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''
from math import sqrt
prime = lambda x:False if [i for i in xrange(2,int(sqrt(x)+1)) if x%i==0] else True
sum(filter(prime, xrange(3,2000000,2)))+2
[/code]
