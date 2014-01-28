[code]
fibonacci = lambda n,a=1,b=1:[b,0][n>0] or fibonacci(n-1,b,a+b)
s = n = f = 0
while f < 4000000:
      f = fibonacci(n)
      if not f%2:
         print f
         s += f
      n += 1
print s
[/code]
