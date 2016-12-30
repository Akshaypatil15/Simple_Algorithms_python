import random
from math import log,ceil
"""
There are two approaches taken, one is recursive another, iterative. While time taken (operations) are the same for both, the space requirement is different whose allocation/deallocation changes the overall performance, and eventually, time.
"""
count=space=0
def sort1(l,): #recursive
  global space
  if len(l)==1: return l
  div=int(len(l)/2)
  space+=div #this is because two more lists are created. len(l)/2 is taken instead of len(l) because these lists exist separately
  list1,list2=l[:div],l[div:]
  l1,l2=sort1(list1),sort1(list2)
  return merge(l1,l2)

def merge(l1,l2):
  """
  This is separated because both the algorithms, iterative & recursive use this one.
  """
  #print(l1,l2)
  global count
  p1,p2,f,l_l1,l_l2=0,0,[],len(l1),len(l2)
  while p1<=l_l1 and p2<=l_l2:
    count+=1
    #although the count itself is taken multiple times, it's only just in terms of m*n
    if p1>=l_l1:
      f+=l2[p2:]
      return f
    elif p2>=l_l2:
      f+=l1[p1:]
      return f
    elif l1[p1]<l2[p2]:
      f.append(l1[p1])
      p1+=1
    else:
      f.append(l2[p2])
      p2+=1
#  print("RETURNING",f)
  return f

def divisions(l,intervals):
  for i in range(ceil(len(l)/intervals)):
    yield l[i*intervals:(i+1)*intervals]

def sort2(l): #iterative
  """
  The algorithm is slightly funny.
  First, you take two values and sort them individually
  Then, taking the two-sorted lists as individual values, sort the group
  """
  global count,space
  space=n=len(l) #insitu algorithm. It may go k*n, but then that's implementation.
  k=int(log(n)/log(2)) #this is the number of iterations it'll take
  bound=2**(k+1)
#  print("N=",n,"k=",k,"bound",bound)
#  print("L",l)
  for i in range(k+1): #merge+sort iterations
    g=2**i #the number of elements to group while sorting
#    print("g",g)
    j=0
    while j<=n:
 #     print(j,j+g)
      l1=j,j+g
      f=l[j:j+g]
  #    print("L1",f)
      j+=g
      if(j<n):
        l2=j,j+g
        f2=l[j:j+g]
       # print("L2",f2)
        l=l[:l1[0]]+merge(f,f2)+l[l2[1]:]
      else:
        l=l[:l1[0]]+f
      j+=g
      
###      if j<n
  return l

if __name__=="__main__":
  n=21
  count=space=0
  print(sort2([random.choice(range(n)) for i in range(n)]))
  print("time:%d,\nspace:%d"%(count,space))
