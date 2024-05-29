import kruskal as kr
import dijkstra as dij

if __name__ == "__main__":
    # variable for input file
    f = None

    while True:
        # get a input file name
        file_name = input("Input file name: ")

        # check if the file name is valid
        try:
            f = open(file_name, "r")
        except FileNotFoundError:
            print("Invalid file name!\n")
        else:
            break

    # split the input file into lines
    lines = f.read().split('\n')
    f.close()

    # city count from the first line
    first = lines[0].split(" ")
    city_count = int(first[0])

    # destination from the second to last line (last is empty)
    destination = int(lines[-2])

    # start node
    start = 1

    # array for graph edges
    edges = []

    # add the edge data from the file into the array
    for line in lines:
        if not line == lines[0] and not line == lines[-1] and not line == lines[-2]:
            values = line.split(" ")
            edges.append((int(values[0])-1, int(values[1])-1, int(values[2])))

    # create minimum spanning tree
    mst = kr.kruskalAlgorithm(edges, city_count)

    # initialize a graph for dijkstra
    g = dij.WeightedGraph(city_count)
    
    # add the edge data from the file into the graph
    for edge in mst:
        dij.add_edge(g, edge[0] + 1, edge[1] + 1, edge[2])

    # find the shortest path
    dij.dijkstraAlgorithm(g, start, destination)

    # print answer
    dij.print_answer(g, destination)