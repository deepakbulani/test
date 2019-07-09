t=input()
print("\n")
while t>0:
 i=0
 j=0
 a=raw_input()
 l=len(a)-2
 ans="0"
 ans1="0"
 while i<l:
  if a[i]=='+':
   for j in range(i+2,l):
    if(a[j]==" "):
      i=i+1
      break
    else:
     i=i+1
     ans1=ans1+a[j]
    i=i+1
   ans=str(int(ans)+int(ans1))
   ans1="0"
  elif(a[i]=='*'):
   for j in range(i+2,l):
    if(a[j]==" "):
      break
    else:
     i=i+1
     ans1=ans1+a[j]
   i=i+1
   ans=str(int(ans)*(int(ans1)))
   ans1="0"
  elif(a[i]=='/'):
   for j in range(i+2,l):
    if(a[j]==" "):
      break
    else:
     i=i+1
     ans1=ans1+a[j]
   i=i+1
   ans=str(int(ans)/int(ans1))
   ans1="0"
  elif(a[i]=='-'):
   for j in range(i+2,l):
    if(a[j]==" "):
      break
    else:
     i=i+1
     ans1=ans1+a[j]
   i=i+1
   ans=str(int(ans)-int(ans1))
   ans1="0"
  elif(a[i]!=" "):
   ans=ans+a[i]
  i=i+1
 print(int(ans))
 print("\n")
 t=t-1
