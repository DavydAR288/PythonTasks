def f(m,n):
 if m==0:
  return (n+1)
 if m>0 and n==0:
  return f(m-1,1)
 if m>0 and n>0:
  return f(m-1,f(m,n-1))
print(f(1,10))