def score(name,score):
 print("%s scored %d marks"%(name,score))
score("mark",85)
def score1(name,*score):
 print(name)
 print(score)
score1("Mark",55,70,90,67)
def score2(*score):
 print(score)
score2(1,2,3,4,5,6,7,8,9,10)
