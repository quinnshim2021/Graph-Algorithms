from collections import defaultdict
from sys import maxsize
import networkx as nx 
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.size = vertices
    
    # start node, end node, weight
    def addEdge(self, u, v, w): 
        self.graph[u].append((v, w))
    
    def draw(self):
        G = nx.DiGraph()
        edges = []
        for startNode in self.graph:
            for edge in self.graph[startNode]:
                edges.append((startNode, edge[0], edge[1])) # start node, end node, weight

        G.add_weighted_edges_from(edges)
        pos = nx.spring_layout(G)
        plt.figure()
        nx.draw(G, pos, edge_color="black", labels={node:node for node in G.nodes()}) # draw nodes
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(i[0], i[1]): i[2] for i in edges}) # draw edges and labels
        plt.axis('off')
        plt.show()

    '''
        Floyd Cycle Determining Algorithms
    '''
    # slow and fast move until they meet
    # NOTE cycle found depends on order edges are added
    def cycleLocation(self, head, collision):
        while True:
            if head == collision:
                print(f"cycle starts at {head}\n")
                return

            head = self.graph[head][0][0]
            collision = self.graph[collision][0][0]

    # fast moves 2 spaces, slow moves 1 space, if they meet there's a collision
    def cycleDetection(self, head):
        slow = fast = head
        count = 0

        while self.graph[fast] and self.graph[self.graph[fast][0][0]]:
            slow = self.graph[slow][0][0]
            fast = self.graph[self.graph[fast][0][0]][0][0]

            print(f"slow at: {slow}, fast at: {fast}")

            if slow == fast:
                print("cycle")
                self.cycleLocation(head, fast)
                return

                
        print("no cycle\n")
        return

    '''
        Breadth First Traversal and Depth First Traversal
    '''
    # go level by level
    def bft(self, head):
        visited = [False] * self.size

        queue = []

        queue.append(head)
        visited[head] = True

        while queue:
            s = queue.pop(0)

            print(f"{s} visited")

            for node in self.graph[s]:
                if visited[node[0]] == False:
                    queue.append(node[0])
                    visited[node[0]] = True
        print()
        return
    
    # for each node, go as right as possible until leaf, then continue
    def dft(self, head):
        visited = [False] * self.size
        stack = []

        stack.append(head)

        while stack:
            s = stack.pop(0)

            if not visited[s]:
                print(f"{s} visited")
                visited[s] = True

            for edge in self.graph[s]:
                if not visited[edge[0]]:
                    stack.insert(0, edge[0])
        print()
        return

    '''
        Binary Tree and Binary Search Tree
    '''
    def bst(self, root):
        stack = [root]
        visited = [False] * self.size
        visited[root] = True

        bst = True

        while stack:
            s = stack.pop(0)

            if len(self.graph[s]) == 2:
                print(self.graph[s][0][0], self.graph[s][1][0])
                if not s > self.graph[s][0][0] or not s < self.graph[s][1][0]:
                    bst = False

                for child in self.graph[s]:
                    if not visited[child[0]]:
                        print(child[0])
                        stack.append(child[0])
            elif len(self.graph[s]) != 0:
                print("Not a Binary Tree or Binary Search Tree\n")
                return
        if bst:
            print("Is a Binary Search Tree\n")
        else:
            print("Is a Binary Tree\n")
        return

    '''
        Minimum Spanning Tree
    '''
    def prims(self, head):
        mstSet = []
        mstSet.append(head)

        totalWeight = 0
        finalTree = []

        while len(mstSet) < self.size:
            minNode = -1
            minWeight = 10000000000000
            f = []

            for node in mstSet:
                for edge in self.graph[node]:
                    if (edge[0] not in mstSet) and (edge[1] < minWeight):
                        minNode = edge[0]
                        minWeight = edge[1]
                        f = [node, edge[0]]
            
            finalTree.append(f)
            mstSet.append(minNode)
            totalWeight += minWeight

        print(f"\nMinimum Spanning Tree Weight: {totalWeight}")
        print("Minimum Spanning Tree Edges:")
        for edge in finalTree:
            print(edge)
        print()
    

                    

            
