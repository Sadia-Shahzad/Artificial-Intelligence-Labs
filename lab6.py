class Graph:
    def __init__(self):
        self.adj={}

    def add_vertex(self,v):
        if v not in self.adj:
            new={"v":[]}
            self.adj.update(new)

    def add_edge(self,v1,v2):
        if v1 in self.adj and v2 in self.adj:
            self.adj[v1].append(v2)
            self.adj[v2].append(v1)
    
    def DFSusingstack(self,S,G):
        stack=[]
        stack.append(S)
        path=[]

        while (stack != []):
            if S==G:
                path.append(S)
                return path
            popped=path.append(stack.pop(S)) 
            stack.append(self.adj[popped])
            S=stack[-1]
        

g=Graph()
g.add_vertex("a")            
g.add_vertex("b")            
g.add_vertex("c")            
g.add_vertex("d")            
g.add_vertex("e")            
g.add_vertex("f")            
g.add_vertex("g")            
g.add_vertex("h")   
g.add_vertex("i")          
g.add_vertex("j")            
g.add_vertex("k")            
g.add_vertex("l")            
g.add_vertex("m")            
g.add_vertex("n")            
g.add_vertex("i")            


g.add_edge("a","b")
g.add_edge("a","f")
g.add_edge("a","d")
g.add_edge("a","e")
g.add_edge("b","k")
g.add_edge("b","j")
g.add_edge("k","n")
g.add_edge("k","m")
g.add_edge("d","g")
g.add_edge("e","c")
g.add_edge("e","h")
g.add_edge("e","i")
g.add_edge("i","l")

print(g.DFSusingstack("a","g"))