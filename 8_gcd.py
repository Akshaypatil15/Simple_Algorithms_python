from math import floor
def gcd(a,b):
  print(a,b)
  if a<b:
    gcd(b,a)
  if b==0: return a
  return gcd(b,a%b)


def gcd_extension(a,b):
  if b==0:
    print("bottoming out @ %d"%a)
    return (a,1,0)
  else:
    d1,x1,y1=gcd_extension(b,a%b)
    print("d1,x1,y1:",d1,x1,y1)
    d,x,y=(d1,y1,x1-floor(a/b)*y1)
    ("d,x,y:",d,x,y)
    return (d,x,y)

if __name__=='__main__':
  a,b=99,78
#  a,b=54,12
  print("gcd",gcd(a,b))
  d,x,y=gcd_extension(a,b)
  print("gcd_extension",d,x,y)
