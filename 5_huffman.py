frequencies={
  'b':1,'p':1,'`':2,'m':2,'j':3,'o':3,'d':3,'a':4,'i':4,'r':5,'u':5,
  'l':6,'s':6,'e':8,'_':12
}

POLICY={
  'left':'1',
  'right':'0',
}

def build_frequencies(string):
  freq={}
  for i in string:
    freq[i]=freq[i]+1 if i in freq else 1
  return freq

"""
inserts inplace
"""
def insert_i(q,item): #could get very very expensive
  q.append(item)
  return q.sort(key=lambda x:x['freq'])

def make_queue(frequencies):
  q=[]
  for c,freq in frequencies.items():
    print("C",c,freq,)
    insert(q,{"left":None,"right":None,"freq":freq,"char":c})
  return q

def build_tree(frequencies):
  q=make_queue(frequencies)
  for i in range(len(q)):
    if(len(q)==1): return q[0]
    node={}
    node["left"]=left=q.pop(0)
    node['right']=right=q.pop(0)
    node['freq']=left["freq"]+right["freq"]
    insert_i(q,node)
    
def insert(q,item): #could get very very expensive
  q.append(item)
  return sorted(q,key=lambda x:x['freq'])  

def huffman(txt):
  #helpers.reset()
  codes=generate_codes(build_tree(build_frequencies(txt)))
  return codes

def build_tree_r(frequencies):
  if type(frequencies) == dict:
    frequencies=make_queue(frequencies) #onetime
  if len(frequencies)==1: return frequencies[0]
  node={}
  node["left"]=left=frequencies.pop(0)
  node['right']=right=frequencies.pop(0)
  node['freq']=left["freq"]+right["freq"]
  return build_tree_r(insert(frequencies,node))

def generate_codes(tree,code='',codes={}):
  if 'char' in tree:
    codes[tree['char']]=code
  for d in 'left','right':
    if tree[d]:
      generate_codes(tree[d],code+POLICY[d],codes)
  return codes

def huffman_r(txt):
  #helpers.reset()
  codes=generate_codes(build_tree_r(build_frequencies(txt)))
  return codes

if __name__=='__main__':
  txt="hellow world"
  print("code for %s: %s"%(txt,huffman(txt)))
