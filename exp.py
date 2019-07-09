def fun(n):
 if(n==0 or n==1):
  return n
 else:
  return fun(n-1)+fun(n-2)
print(fun(3))
