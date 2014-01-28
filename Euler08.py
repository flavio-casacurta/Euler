for i in xrange(0, len(s)-4):
    p = 1
    for j in xrange(i,i+5):
        p = p * int(s[j])
    if p > n: n = p

print n


print max(map(lambda slc:reduce(lambda x,y:x*y,[int(i) for i in slc]),[s[e:e+5] for e,n in enumerate(s) if e+4 < len(s)]))
