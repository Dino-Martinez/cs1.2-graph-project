# This class will represent our graph of courses
from node import Node
from edge import Edge

class Graph:

    def __init__(self):
        self._nodes = []
        self._edges = []


    def add_node(self, data):
        self._nodes.append(Node(data))

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

    def prereqs(self, course, prerequisites=[]):
        try:
            this_index = self._nodes.index(Node(course))
            this_node = self._nodes[this_index]
            edges = this_node.get_edges()
            if len(edges) > 0:
                for _ in range(len(edges)):
                    if edges[_]._to._data not in prerequisites:
                        prerequisites.append(edges[_]._to._data)
                    self.prereqs(edges[_]._to._data, prerequisites)
        except:
            print("The requested course doesn't exist")
        return prerequisites

    def print_nodes(self):
        for _ in range(len(self._nodes)):
            print(self._nodes[_]._data)

    def print_edges(self):
        for _ in range(len(self._edges)):
            print(f"({self._edges[_]._from._data}, {self._edges[_]._to._data})")
