[code]
from math import sqrt
prime = lambda x:False if [i for i in xrange(2,int(sqrt(x)+1)) if x%i==0] else True
n = 2
c = 0
while c < 10001:
    if prime(n):
        p=n
        c+=1
    n+=1
print p
[/code]
