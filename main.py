#This is my new.py in this program it takes only uni direction paths and connect them. 
# It works properly for finding the shortest paths and distance between them.
#This is integrated with shortest_path.html which includes java script as well
from flask import Flask, request, render_template

app = Flask(__name__)
GGRAPH = None

class Node:
    def __init__(self, name):
        self.name = name.lower()
        print("name",name)

class Edge:
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
        print(f"Distance between from Node {from_node} to Node {to_node} is {weight}")

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        print("{0}: Graph: {1}, {2}".format("Graph", len(self.nodes), len(self.edges)))

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        for edge in self.edges[from_node]:
            if edge.to_node == to_node:
                return  # Edge already exists, ignore duplicate
        self.edges[from_node].append(Edge(from_node, to_node, weight))
        print(f'(The weight from node {from_node} to node {to_node} is {weight})')


def create_graph_from_form(form):
    graph = Graph()

    num_nodes = int(form.get('num_nodes', 0))
    num_edges = int(form.get('num_edges', 0))

    for i in range(num_nodes):
        node_name = form.get(f'node_{i}', '').lower()
        print(f'(Node name: {node_name})')
        if node_name:
            node = Node(node_name)
            graph.add_node(node)

    for i in range(num_edges):
        from_node = form.get(f'from_node_{i}', '').lower()
        to_node = form.get(f'to_node_{i}', '').lower()
        weight = int(form.get(f'weight_{i}', 0))

        if from_node and to_node:
            graph.add_edge(from_node, to_node, weight)
            
    return graph

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra(graph, initial, end):
    print("Starting the Algorithm")
    shortest_paths = {initial: (None, 0)}  # Dictionary to store the shortest path and distance to each node  
    current_node = initial    # Start with the initial node
    visited = set()  # Set to keep track of visited nodes

    while current_node != end:
        visited.add(current_node)     # Mark the current node as visited
        destinations = [edge.to_node for edge in graph.edges.get(current_node, [])]    # Get the destination nodes from the current node's edges
        weight_to_current_node = shortest_paths[current_node][1]   # Get the weight to the current node
        print(f'Current node is: {current_node}, Next destinations are: {destinations} and Weight to current node is: {weight_to_current_node}')
        
        # Iterate over the next nodes and update the shortest paths
        for next_node in destinations:
            print(f"Next Node:{next_node}")
            edge = next(
                edge for edge in graph.edges[current_node]
                if edge.to_node == next_node )     # Find the edge between the current node and the next node
            weight = edge.weight + weight_to_current_node  # Calculate the weight to the next node
            print("Weight to the next node is: ",weight)

            # Update the shortest paths if a shorter path is found
            if next_node not in shortest_paths:
                print(f'Next Node:{next_node} and Shortest Paths:{shortest_paths}')
                shortest_paths[next_node] = (current_node, weight)
                print(f'{shortest_paths[next_node]}={current_node,weight}')
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                print(f'Current shortest weight:{current_shortest_weight}')
                if current_shortest_weight > weight:
                    print(f'{current_shortest_weight} is greater than {weight}')
                    shortest_paths[next_node] = (current_node, weight)
                    print(f'Updated shortest path {current_node} to node {next_node}')

        # Get the next possible destinations
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        print(f'Next destinations: {next_destinations}')
        if not next_destinations:
            break

        # Select the next node with the smallest distance
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
        print("current_node_to_find_min",current_node)

    path = []    # List to store the shortest path
    distance = shortest_paths.get(end, (None, None))[1]    # Get the distance to the end node
    print("shorted_distance_to_the_end_node",distance)

    # Reconstruct the shortest path
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node

    print(f'Received Path:{path}')
    path = path[::-1]      # Reverse the path to get the correct order
    print("path,distance",path,distance)
    return path, distance


@app.route('/')
def index():
    return render_template('shortest_path.html')

@app.route('/create_graph', methods=['POST'])
def create_graph():
    print("{0}: Request received: {1}, {2}".format("create_graph", request.method, request.form))
    global GGRAPH
    GGRAPH = create_graph_from_form(request.form)
    print(f'GGRAPH:{GGRAPH}') 
    return render_template('path_finder.html', graph=GGRAPH)

@app.route('/path_finder', methods=['POST'])
def path_finder():
    print("{0}: Request received: {1}, {2}".format("path_finder", request.method, request.form))
    source = request.form.get('source', '').lower()
    destination = request.form.get('destination', '').lower()

    if source == "" or destination == "":
        return render_template('missing.html', source=source, destination=destination)
    
    if GGRAPH is None:
        return render_template('fault.html', source=source, destination=destination)
    
    if source in GGRAPH.nodes and destination in GGRAPH.nodes:
        forward_edge_exists = any(
            edge.to_node == destination for edge in GGRAPH.edges.get(source, [])
        )
        if not forward_edge_exists:
            return render_template('missing.html', source=source, destination=destination)

    path, distance = dijkstra(GGRAPH, source, destination)

    if path is None or distance is None:
        return render_template('fault.html', source=source, destination=destination)
    else:
        path_dirr = '=>'.join(path).upper()
        return render_template('output.html', path_dirr=path_dirr, distance=distance)

if __name__ == '__main__':
    app.run(debug=True, port=5556)