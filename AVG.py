t=input()
i=0
ans=0
while i<t:
 j=0
 a=input()
 b=raw_input()
 while j<len(b):
   ans=ans+int(b[j])
   j=j+2
 print(ans/a)
