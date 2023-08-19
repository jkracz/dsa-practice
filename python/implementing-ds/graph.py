class Graph:
    def __init__(self) -> None:
        self.number_of_nodes = 0
        self.adjacency_list = dict()

    def addVertex(self, node):
        self.adjacency_list[node] = []
        self.number_of_nodes += 1

    def addEdge(self, node1, node2):
        # undirected
        if node1 in self.adjacency_list.keys() and node2 in self.adjacency_list.keys():
            self.adjacency_list[node1].append(node2)
            self.adjacency_list[node2].append(node1)
        else:
            print("both verticies must exist")

    def showConnections(self):
        all_nodes = list(self.adjacency_list.keys())
        for node in all_nodes:
            node_connections = self.adjacency_list[node]
            connections = ""
            for vertex in node_connections:
                connections += str(vertex) + " "
            print(f"{node} --> {connections}")


# class Graph {
#   constructor() {
#     this.numberOfNodes = 0;
#     this.adjacentList = {
#     };
#   }
#   addVertex(node)  {
#   }
#   addEdge(node1, node2) {
#     //undirected Graph
#   }
#   showConnections() {
#     const allNodes = Object.keys(this.adjacentList);
#     for (let node of allNodes) {
#       let nodeConnections = this.adjacentList[node];
#       let connections = "";
#       let vertex;
#       for (vertex of nodeConnections) {
#         connections += vertex + " ";
#       }
#       console.log(node + "-->" + connections);
#     }
# }
# }

myGraph = Graph()
myGraph.addVertex("0")
myGraph.addVertex("1")
myGraph.addVertex("2")
myGraph.addVertex("3")
myGraph.addVertex("4")
myGraph.addVertex("5")
myGraph.addVertex("6")
myGraph.addEdge("3", "1")
myGraph.addEdge("3", "4")
myGraph.addEdge("4", "2")
myGraph.addEdge("4", "5")
myGraph.addEdge("1", "2")
myGraph.addEdge("1", "0")
myGraph.addEdge("0", "2")
myGraph.addEdge("6", "5")

myGraph.showConnections()
# Answer:
# 0-->1 2
# 1-->3 2 0
# 2-->4 1 0
# 3-->1 4
# 4-->3 2 5
# 5-->4 6
# 6-->5
