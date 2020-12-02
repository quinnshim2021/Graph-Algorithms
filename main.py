from Graph import Graph
'''
    All nodes must start at 0 and only increment by 1
    Must have number of vertices correct, if updating later we can update that variable
'''

# directed or undirected, unweighted graph
def runFloyd():
    g = Graph(5)
    g.addEdge(0, 1, 0)
    g.addEdge(1, 2, 0)
    g.addEdge(2, 3, 0)
    g.addEdge(3, 4, 0)

    # 0 -> 1 -> 2 -> 3 -> 4
    g.cycleDetection(0) # 0 is start node

    g.addEdge(4, 3, 0)
    
    # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 3...
    g.cycleDetection(0)

# directed or undirected, unweighted graph
def runBFT():
    g = Graph(5)
    g.addEdge(0, 1, 0)
    g.addEdge(0, 2, 0)
    g.addEdge(0, 3, 0)
    g.addEdge(1, 0, 0)
    g.addEdge(2, 0, 0)
    g.addEdge(3, 0, 0)
    g.addEdge(2, 4, 0)
    g.addEdge(4, 3, 0)
    
    g.bft(0)

# undirected or undirected, unweighted graph
def runDFT():
    g = Graph(5)
    g.addEdge(0, 1, 0)
    g.addEdge(0, 2, 0)
    g.addEdge(0, 3, 0)
    g.addEdge(1, 0, 0)
    g.addEdge(2, 0, 0)
    g.addEdge(3, 0, 0)
    g.addEdge(2, 4, 0)
    g.addEdge(4, 3, 0)

    g.dft(0)

# directed (no two-way edges), a-cyclic, unweighted graph
def runBST():
    g = Graph(6)
    g.addEdge(3, 1, 0)
    g.addEdge(3, 4, 0)
    g.addEdge(1, 0, 0)
    g.addEdge(1, 2, 0)

    # BST
    g.bst(3)

    g.addEdge(4, 5, 0)
    g.addEdge(4, 0, 0)

    # BT
    g.bst(3)

    g.addEdge(2, 5, 0)

    # Nothing
    g.bst(3)

# undirected, weighted graph
def runPrim():
    g = Graph(9)
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 0, 4)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(7, 0, 8)
    g.addEdge(7, 1, 11)
    g.addEdge(7, 8, 7)
    g.addEdge(7, 6, 1)
    g.addEdge(2, 1, 8)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(2, 3, 7)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(6, 5, 2)
    g.addEdge(8, 2, 2)
    g.addEdge(8, 6, 6)
    g.addEdge(8, 7, 7)
    g.addEdge(5, 6, 2)
    g.addEdge(5, 2, 4)
    g.addEdge(5, 3, 14)
    g.addEdge(5, 4, 10)
    g.addEdge(3, 2, 7)
    g.addEdge(3, 5, 14)
    g.addEdge(3, 4, 9)
    g.addEdge(4, 3, 9)
    g.addEdge(4, 5, 10)

    g.prims(0)

def run():
    while True:
        option = input(
            """Select an algorithm:
    1. Floyd's cycle determining/locating
    2. Breadth First Traversal
    3. Depth First Traversal
    4. Is Binary Tree?
    5. Prim's Minimum Spanning Tree
    x. Quit
    : """)
        if option == "1":
            runFloyd()
        elif option == "2":
            runBFT()
        elif option == "3":
            runDFT()
        elif option == "4":
            runBST()
        elif option == "5":
            runPrim()
        elif option == "x":
            return

if __name__ == "__main__":
    run()

