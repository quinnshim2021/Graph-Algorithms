from Graph import Graph
'''
    problems:
        BT/BST aren't working (problem with undirected graphs, roots other than 0)
    
    important notes:
        nodes must start at 0 and increment by 1
            problems if not true
        if weights for same edge differ, last edge's weight will be used
'''
# default to some Graph, will be global graph used for all operations
g = Graph(3)
g.addEdge(0, 1, 0)
g.addEdge(0, 2, 4)

def create():
    global g

    warning = input("Warning: Creating a new graph will replace current graph. Is this okay? y/n ")

    if warning == "y":
        nodes = int(input("How many nodes? Must ensure this is correct. "))
        g = Graph(nodes)

        creating = "y"
        print("\nGraph is created by creating edges. Will enter start node, end node, and the weight between them\n")

        while creating == "y":
            start = int(input("Enter starting node: "))
            end = int(input("Enter ending node: "))
            weight = int(input("Enter edge weight: "))
            g.addEdge(start, end, weight)

            creating = input("Add another edge? y/n ")
            

# directed or undirected, unweighted graph
# takes in start node
def runFloyd():
    global g

    if g != None:
        start = int(input("Which node is the starting node? "))
        g.cycleDetection(start)

# directed or undirected, unweighted graph
# takes in root node
def runBFT():
    global g

    if g != None:
        root = int(input("Which node is the root? "))
        g.bft(root)

# undirected or undirected, unweighted graph
# takes in root node
def runDFT():
    global g

    if g != None:
        root = int(input("Which node is the root? "))
        g.dft(root)

# directed (no two-way edges), a-cyclic, unweighted graph
# bst takes in root node
def runBST():
    global g

    if g != None:
        root = int(input("Which node is the root? "))
        g.bst(root)

# undirected, weighted graph
# prims takes in start node
def runPrim():
    global g
    
    if g != None:
        start = int(input("Which node is the start node? "))
        g.prims(start)

# draws graph
def runDraw():
    global g

    if g != None:
        g.draw()

# rules of program
def printHowTo():
    print("\nRules: Nodes and weights must be represented as integers. Nodes must start at 0 and increment by 1. It is important to have number of nodes correct in 'Create'. \nGraph will be undirected if you create an edge each way.\n")

def run():
    while True:
        option = input(
            """Select an algorithm:
    1. Create Graph
    2. Draw Current Graph
    3. Floyd's Cycle Determining/Locating Algorithm
    4. Breadth First Traversal
    5. Depth First Traversal
    6. Is Binary Tree?
    7. Prim's Minimum Spanning Tree
    8. How To
    x. Quit
    : """)
        if option == "1":
            create()
        elif option == "2":
            runDraw()
        elif option == "3":
            runFloyd()
        elif option == "4":
            runBFT()
        elif option == "5":
            runDFT()
        elif option == "6":
            runBST()
        elif option == "7":
            runPrim()
        elif option == "8":
            printHowTo()
        elif option == "x":
            return

if __name__ == "__main__":
    run()

