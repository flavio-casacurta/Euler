import urllib2
import re
URL = 'http://projecteuler.net/problem=8'
page = urllib2.urlopen(URL).read()
lst = re.findall(r'\d{50}', page)
s = ''.join(lst)
print max(map(lambda slc:reduce(lambda x,y:x*y,[int(i) for i in slc]),
              [s[e:e+13] for e, n in enumerate(s) if e+12 < len(s)]))
