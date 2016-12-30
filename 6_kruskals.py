count=0
def make_set(collection,element):
  if type(element)!=set:
    element={element}
  for each_set in collection:
    if each_set==element:
      #print("already belonging in the collection")
      return False
  collection.append(element)
  return True

  
def find_set(collection,element):
  for each_set in collection:
    if element in each_set:
      return each_set
  raise Exception("Should not be here!!!")
  return None 

def union(collection,subset1,subset2):
  collection.remove(subset1)
  collection.remove(subset2)
  collection.append(subset1.union(subset2))

def add(G,v):
  if v not in G['V']:
    G['V'].append(v)

def init(graph):
  G={}
  G['V'],G['E']=[],[]
  for vertex,branches in graph.items():
    add(G,vertex)
    for vertex2,weight in branches.items():
      add(G,vertex2)
      G['E'].append({'edge':(vertex,vertex2),'weight':weight})
  return G
  
def kruskals(G):
  disjoint_set,A,spanning_weight=[],set(),0
  for vertex in G['V']:
    make_set(disjoint_set,vertex)
  for edge in sorted(G['E'],key=lambda x:x['weight']):
    e1,e2=edge['edge'][0],edge['edge'][1]
    r1,r2=find_set(disjoint_set,e1),find_set(disjoint_set,e2) #representations
    #print("E",edge,r1,r2)
    if r1 != r2:
      #print("NEW",e1,e2)
      A=A.union({(e1,e2)})
      spanning_weight+=edge['weight']
      union(disjoint_set,r1,r2)
    #else:
      #print("OLD",e1,e2)
    #print("collection",disjoint_set)
    #print("A",A)
  return A,spanning_weight

if __name__=='__main__':
  graph2={'a':{'b':4,'c':2},'b':{'c':1,'d':5,},'c':{'d':8,'e':10},\
          'd':{'e':2,'z':6},'e':{'z':3}}
  graph3={'a':{'b':4,'h':8},
          'b':{'c':8,'h':11},
          'c':{'d':7,'f':4,'i':2,},
          'd':{'e':9,'f':14},
          'e':{'f':10},
          'f':{'g':2,},
          'g':{'i':6,'h':1},
          'h':{'i':7}
          }
  print("For graph",graph3)
  print(kruskals(init(graph3)))
