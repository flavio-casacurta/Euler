[code]
r0 = lambda x: x%3 == 0 or x%5 == 0
%%timeit -n10000
m35=0
for n in xrange(1,1000):
    if  r0(n):
        m35 += n

#10000 loops, best of 3: 205 탎 per loop

%%timeit -n10000
sum([x for x in xrange(1,1000) if r0(x)])
#10000 loops, best of 3: 209 탎 per loop

%%timeit -n10000
sum([x for x in xrange(1,1000) if x%3 == 0 or x%5==0])
#10000 loops, best of 3: 107 탎 per loop
#  <<< the best result >>>

%%timeit -n10000
reduce(lambda x,y: x+y, filter(r0, xrange(1000)))
#10000 loops, best of 3: 228 탎 per loop

%%timeit -n10000
reduce(lambda x,y: x+y, filter(lambda n: n%3==0 or n%5==0, range(1000)))
#10000 loops, best of 3: 228 탎 per loop
[/code]



