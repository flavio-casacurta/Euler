from math import sqrt
prime = lambda x:False if [i for i in xrange(2,int(sqrt(x)+1)) if x%i==0] else True
fibonacci = lambda n,a=1,b=1:[b,0][n>0] or fibonacci(n-1,b,a+b)
product = lambda line: reduce(lambda x, y: x*y, line)
