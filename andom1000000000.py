import random
z=0
c=0

for w in range(1000000000):
  q=random.randint(0,9)
  if q==0:
    z+=1
  elif q==1 or q==2:
    z+=1
  elif q==3 or q==4 or q==5:
    c+=1
  else:
    z+=1
#q=3,4,5 -> vic
print("lo")
print(z) 
print("vic")
print(c) 
