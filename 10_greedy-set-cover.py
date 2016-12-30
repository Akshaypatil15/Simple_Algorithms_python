def setcover(S,F): #S the universe, F the set of sets, based on CLRS
  U=S
  C=[] #init blank
  while len(U) != 0:
    s=max(F,key=lambda f:len(f.intersection(U)))
    print(s)
    U=U.difference(s)
    C.append(s)
  return C
    

if __name__=='__main__':
  #problem instance from pg. 1118
  """
  a b c
  d e f
  g h i
  j k l
  """
  S=set("abcdefghi")
  F=[set('abcdef'), #1
     set('efhi'), #2
     set("adgj"), #3
     set("beghk"), #4
     set("cfil"), #5
     set("jk"), #6
  ]
  print("Set Cover",setcover(S,F))
