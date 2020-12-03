# This class will represent a single Node in our Graph
from edge import Edge

class Node:
    def __init__(self, data):
        self._data = data
        self._edges = []

    def get_edges(self):
        return self._edges

    def add_edge(self, node):
        edge = Edge(self, node)
        self._edges.append(edge)
        return edge

    def get_data(self):
        return self._data

    def __eq__(self, other):
        if self.get_data() == other.get_data():
            return True

        return False
