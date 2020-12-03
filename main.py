# We will run our code from here
from graph import Graph

my_graph = Graph()
my_graph.add_edge('from', 'to')
my_graph.add_edge('second', 'to')
my_graph.add_edge('second', 'from')
my_graph.add_edge('second', 'third')
my_graph.add_edge('third', 'to')
#my_graph.print_edges()
#my_graph.print_nodes()
my_graph.print_connections('second')
