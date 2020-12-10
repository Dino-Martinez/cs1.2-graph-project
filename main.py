# We will run our code from here
from graph import Graph
import json


def json_to_graph(file):
    graph = Graph()
    json_file = open(file)
    data = json.load(json_file)
    for i in range(len(data)):
        current = data[i]["name"]
        graph.add_node(current)
        for j in range(len(data[i]["prerequisites"])):
            connection = data[i]["prerequisites"][j]
            graph.add_edge(current, connection)

    return graph


my_graph = Graph()
my_graph = json_to_graph('data.json')
my_graph.print_nodes()
course = 'FEW 2.4'
print(f"Prerequisites for {course}: ")
print(my_graph.prereqs(course))
