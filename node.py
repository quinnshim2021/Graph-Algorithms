from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v, w): # start node, end node, weight
        self.graph[u].append((v, w))
    
    def getSize(self):
        return len(self.graph)
