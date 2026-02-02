import heapq
class Node:
    def __init__(self , name , coordinates , heuristic=0):
        self.name = name
        self.coordinates = coordinates
        self.heuristic = heuristic
    def __lt__(self , x):
        return self.heuristic < x.heuristic
    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return (self.name, self.heuristic) == (other.name, other.heuristic)

    def __hash__(self):
        return hash((self.name, self.heuristic))
    def __repr__(self):
        return str(self.name)
def dist(a , b):
    return (abs(a.coordinates[0]-b.coordinates[0])**2 + 
            abs(a.coordinates[1]-b.coordinates[1])**2)**0.5
class Graph:
    def __init__(self , nodes , directed , *edges):
        self.n = len(nodes)
        self.nodes = nodes
        self.adj  = {}
        for node in self.nodes:
            self.adj[node.name] = []
        for edge in edges:
                self.adj[edge[0].name].append(edge[1])
                if(directed==False): self.adj[edge[1].name].append(edge[0])
    def a_star_search(self , root , goal):
        for node in self.nodes:
            node.heuristic = dist(node , goal)
        open_list = []
        closed_list = {}
        heapq.heappush(open_list , (root.heuristic , 0 , [] , root))
        ans , final_path = None , None
        while(len(open_list)):
            f , g , path , top = heapq.heappop(open_list)
            ans,  final_path = top , path+[top]
            if(top==goal): break
            for node in self.adj[top.name]:
                if(node in closed_list.keys()):
                    if(closed_list[node] > g + 1 + node.heuristic):
                        heapq.heappush(open_list , 
                                       (g+1+node.herustic , g+1 , path+[top] , node))
                elif(node not in open_list):
                    heapq.heappush(open_list ,
                                   (g+1+node.heuristic , g+1 ,path+[top],node))
                else: continue
            closed_list[top] = g + node.heuristic 
        return final_path
def main():        
    A = Node('A' , (1,2))
    B = Node('B' , (0 , 1))
    C = Node('C' , (2,1))
    D = Node('D' , (-1,0))
    E = Node('E' , (1,0))
    F = Node('F' , (3,0))
    g = Graph([A , B , C , D , E , F] , False , (A , B) , (A,C) , (B,D) , (B,E),(C,F))
    ans = g.a_star_search(A , F)
    print(ans)
main()