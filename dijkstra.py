INF = float('inf')

class WeightedEdgeNode:
	def __init__(self, n, w = 0):
		self.node = n
		self.weight = w

class WeightedGraph:
    def __init__(self, nVerts):
        # initialize lists
        self.nVertices = nVerts
        self.adj_list = {}
        self.dist = {}
        self.pred = {}
        self.max = {}
        self.vertices = []
		
        for x in range(1, nVerts+1):
            self.adj_list[x] = []
            self.vertices.append(x)  
            self.dist[x] = INF 
            self.pred[x] = 0
            self.max[x] = INF
            	
def add_edge(g, x, y, w):
    # add an edge to the graph
	g.adj_list[x].append(WeightedEdgeNode(y,w))
	g.adj_list[y].append(WeightedEdgeNode(x,w))

def dijkstraAlgorithm(g, s, d):
    for i in g.vertices:
        g.dist[i] = INF
        g.pred[i] = 0

    g.dist[s] = 0
    g.max[s] = 0

    queue = g.vertices

    while len(queue) > 0:
        minval = INF
        u = 0
        for vert in queue:
            if g.dist[vert] < minval:
                minval = g.dist[vert]
                u = vert
        if u == 0:
            break
        queue.remove(u)			

        for edge in g.adj_list[u]:
            v = edge.node
            if g.dist[v] > g.dist[u] + edge.weight:
                g.max[v] = edge.weight
                g.dist[v] = g.dist[u] + edge.weight
                g.pred[v] = u

def print_answer(g, d):
    # array for path
    path = []

    # array for path's edge weights
    path_max = []

    def make_path(g, dest):
        if g.pred[dest] != 0:
            make_path(g, g.pred[dest])
        path.append(dest)
        path_max.append(g.max[dest])

    # create a path array
    make_path(g, d)

    # check if path was actually found
    path_max.sort()
    if path_max[-1] == INF:
        # print error message
        print("Path was not found!")
    else:
        # print path
        print("\n", end='')
        print("Best route: ", end='')
        for x in path:
            print(x, end='')
            if x != path[-1]:
                print("->", end='')

        # print the biggest weight value of the edges
        print("\nMax height:", path_max[-1])
