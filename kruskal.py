parent = {}
 
# make-set operation
def makeSet(N):
    # create sets for each vertex
    for i in range(N):
        parent[i] = -1

# find the root of the set
def findSet(x):
    # if x is root
    if parent[x] == -1:
        return x

    # recursion until the root is found
    return findSet(parent[x])

def union(a, b):
    # find the root of the sets
    x = findSet(a)
    y = findSet(b)

    parent[x] = y

def kruskalAlgorithm(edges, N):
    # minimum spanning tree
    MST = []

    # create sets for each vertex
    makeSet(N)

    # index for going through edges
    index = 0

    # variable for counting edges in the mst
    mst_index = 0
 
    # sort edges by increasing weight
    edges.sort(key=lambda x: x[2])
 
    # mst has N-1 edges
    while mst_index < N - 1:
        if index == len(edges)-1:
            break

        # get the next edge from the edge array
        (x, y, w) = edges[index]

        # increment index for next loop
        index += 1
 
        # find the root of the sets
        xx = findSet(x)
        yy = findSet(y)
 
        # check if vertexes have a common root
        if xx != yy:
            mst_index += 1          # increment edge count in mst
            MST.append((x, y, w))   # add the edge to mst array
            union(xx, yy)           # union of the two sets
 
    return MST