mpp=0
for n1 in xrange(100,1000):
    for n2 in xrange(100,1000):
        p = n1 * n2
        if  str(p) == str(p)[::-1]:
            if  p > mpp:
                nn1 = n1
                nn2 = n2
                mpp = p
print 'o maior produto palindrome de tres numeros e {} * {} = {}'.format(nn1, nn2, mpp)
