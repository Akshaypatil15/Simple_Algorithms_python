import random
LB,UB=0,1000
def euclid(certificate):
  """
  We'll consider euclid's "first theorem", which states that if a prime number divides product of two numbers, the prime number should divide at least one of the two
  """
  p,a,b=certificate['p'],certificate['a'],certificate['b']
  if (a*b)%p==0:
    if a%p == 0 or b%p == 0:
      return True
    else:
      return False
  else: #this ise because the 
    raise Exception("Bad certificate, p must divide a*b")
  pass

def fermat(certificate):
  """
  Fermat's little theorem.
  Somewhat funny congruence between any number raised to prime number and the modulo of the prime over the same.
  """
  p,a=certificate['p'],certificate['a']
  if (a**(p-1)-1)%p==0:
    return True
  else:
    return False

def verify(problem_name,certificate):
  print("certificate on",problem_name,"=",certificate)
  problem=eval(problem_name)
  if problem(certificate):
    print(problem_name,"verified for the certificate")

if __name__=="__main__":
  verify("euclid",{"p":23,'a':1932,'b':435})
  verify("fermat",{"p":23,'a':random.randint(LB,UB)})
