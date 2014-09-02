import urllib2
import re
URL = 'http://projecteuler.net/problem=11'
page = urllib2.urlopen(URL).read()
npage=re.sub(r'<span style="color:#ff0000;"><b>', '', page)
npage=re.sub(r'</b></span>', '', npage)
f = re.findall(r'((\d{2}\s){19}\d{2})', npage)
l = [f0[0] for f0 in f]
n = [[int(x) for x in y.split()] for y in l]
prod = lambda v, x, y, z : v * x * y * z
print max(
max(prod(n[l][c], n[l][c+1], n[l][c+2], n[l][c+3]) for l in xrange(20) for c in xrange(17)),
max(prod(n[l][c], n[l+1][c], n[l+2][c], n[l+3][c]) for l in xrange(17) for c in xrange(20)),
max(prod(n[l][c], n[l+1][c+1], n[l+2][c+2], n[l+3][c+3]) for l in xrange(17) for c in xrange(17)),
max(prod(n[l][c], n[l+1][c-1], n[l+2][c-2], n[l+3][c-3]) for l in xrange(17) for c in xrange(3,20)))
