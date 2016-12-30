import random
count=0
def my_min(l):
  #this returns the index
  global count
  count+=len(l) #O(n) operation
  return l.index(min(l))

def swap(l,a,b):
  global count
  count+=1
  l[a],l[b]=l[b],l[a]

def permute_random(l): #(i) sorting
  n=len(l)
  random_keys=[random.randint(0,10**n) for i in l]
#  print("keys",random_keys)
  for i in range(n):
    k=my_min(random_keys)
    swap(l,i,k-i)
    random_keys.pop(k)
  return l

def permute_cyclic(l,forward=True): #(ii) cyclic
  k=random.randint(0,len(l)-1)
  if forward: return l[k:]+l[:k]
  else: return l[-k:]+l[:-k]
  

if __name__=="__main__":
  n=10
  l=[random.choice(range(n)) for i in range(n)]
  print("List:%s"%l)
  print("(i) permute-by-sorting: %s"%permute_random(list(l)))
  print("(ii) permute-by-cyclic: %s"%permute_cyclic(list(l)))
