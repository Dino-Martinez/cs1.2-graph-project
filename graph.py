# This class will represent our graph of courses
from node import Node
from edge import Edge

class Graph:

    def __init__(self):
        self._nodes = []
        self._edges = []


    def add_node(self, node):
        self._nodes.append(node)

    def add_edge(self, from_data, to_data):
        # build nodes, append to node list if necessary
        # then build edge and append
        from_node = None
        to_node = None
        try:
            from_index = self._nodes.index(Node(from_data))
            from_node = self._nodes[from_index]
        except:
            from_node = Node(from_data)
            self.add_node(from_node)

        try:
            to_index = self._nodes.index(Node(to_data))
            to_node = self._nodes[to_index]
        except:
            to_node = Node(to_data)
            self.add_node(to_node)

        edge = from_node.add_edge(to_node)
        self._edges.append(edge)

    def print_connections(self, data):
        try:
            this_index = self._nodes.index(Node(data))
            this_node = self._nodes[this_index]
            edges = this_node.get_edges()
            for _ in range(len(edges)):
                print(f"{this_node._data} -> {edges[_]._to._data}")
                #self.print_connections(edges[_]._to._data)
        except:
            print("The requested node doesn't exist")

    def print_nodes(self):
        for _ in range(len(self._nodes)):
            print(self._nodes[_]._data)

    def print_edges(self):
        for _ in range(len(self._edges)):
            print(f"({self._edges[_]._from._data}, {self._edges[_]._to._data})")
