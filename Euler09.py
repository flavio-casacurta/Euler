def euler09(n):
    for i in xrange(1,n,1):
        for j in xrange(1,n-i,1):
            s = n - i - j
            if i**2 + j**2 == s**2:
                return i, j, s, i*j*s
    return 0,0,0,0

