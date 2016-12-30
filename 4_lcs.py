a=list(range(10))
b=(2,5,9)
c=(5,2,1)
d=(3,2,7,8,9)

#largest common subsequence
#untested, unproven!
def lcs(a,b):
  print("(a,b)=",(a,b))
  state=0
  sequences=[[]]
  for i in a:
    if i in b:
      sequences[0].append(i)
    else:
      if(len(sequences[0]) is not 0):
        sequences.insert(0,[])
  print("all sequences",sequences)
  return max(sequences,key=len)
  return sequences

if __name__=='__main__':
  print("LCS:",lcs(a,b))
