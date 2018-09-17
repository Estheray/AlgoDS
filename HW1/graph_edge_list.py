# Please see instructions.txt for the description of this problem.
from exceptions import NotImplementedError

# An implementation of a weighted, directed graph as an edge list. This means
# that it's represented as a list of tuples, with each tuple representing an
# edge in the graph.
class Graph:

  def __init__(self):
    # DO NOT EDIT THIS CONSTRUCTOR
    self.graph = []

  def add_edge(self, node1, node2, weight):
    # Adds a directed edge from `node1` to `node2` to the graph with weight
    # defined by `weight`.
    if (node1,node2,weight) not in self.graph:
        self.graph += [(node1,node2,weight)]

    # raise NotImplementedError

  def has_edge(self, node1, node2):
      return (node1, node2) in [(x,y) for (x,y,z) in self.graph]

    # Returns whether the graph contains an edge from `node1` to `node2`.
    # DO NOT EDIT THIS METHOD
    # return (node1, node2) in [(x,y) for (x,y,z) in self.graph]

  def get_neighbors(self, node):
      # Returns the neighbors of `node` as a list of tuples [(x, y), ...] where
      # `x` is the neighbor node, and `y` is the weight of the edge from `node`
      # to `x`.
      return [(node2,weight) for (node1,node2,weight) in self.graph if node1==node]
  def get_outnodes(self):
      return set([node1 for (node1,node2,weight) in self.graph])
    # Returns the neighbors of `node` as a list of tuples [(x, y), ...] where
    # `x` is the neighbor node, and `y` is the weight of the edge from `node`
    # to `x`.
    # return [(node2,weight) for (node1,node2,weight) in self.graph if node1==node]

  # def get_outnodes(self):
  #     return set([node1 for (node1,node2,weight) in self.graph])

    # raise NotImplementedError

# if __name__ == "__main__":
#     g = Graph()
#     g.add_edge(1,2,34)
#     g.add_edge(1,5,67)
#     print(g.graph)
#     print g.has_edge(1,2)
#     print g.has_edge(1,8)
#     print g.get_neighbors(1)
