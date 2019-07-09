class Person:
 def __init__(self,id):
  self.id=id
  print("our class is created")
 def __del__(self):
  print("our class object is destroyed")
  print(self.id)
 def setFullName(self,fn,ln):
  self.fn=fn
  self.ln=ln
 def printFullname(self):
  print("%s %s"%(self.fn,self.ln))
p = Person(5)
p.setFullName("programming","knowledge")
p.printFullname()
