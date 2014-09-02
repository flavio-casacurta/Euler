r0 = lambda x: x%3 == 0 or x%5 == 0
m35=0
for n in xrange(1,1000):
    if  r0(n):
        m35 += n
print m35

print sum([x for x in xrange(1,1000) if r0(x)])

print sum([x for x in xrange(1,1000) if x%3 == 0 or x%5==0])

print reduce(lambda x,y: x+y, filter(r0, xrange(1000)))

print reduce(lambda x,y: x+y, filter(lambda n: n%3==0 or n%5==0, range(1000)))




