# Please see instructions.txt for the description of this problem.
from exceptions import NotImplementedError
from graph_adjacency_list import Graph as AdjacencyGraph
from graph_edge_list import Graph as EdgeGraph

#TODO: needs to be rethought...no other methods permitted
#if not yet in dict, return "inf" distance, indicates not explored


#TODO remove print comments for testing

def shortest_path(graph, source, target):
    #how to global---without need to pass into distance, without constructor?
    #dict of distances from s
    d = {}
    #set of explored nodes
    S = set()
    #set of unexplored nodes
    Q = set()
# `graph` is an object that provides a get_neighbors(node) method that returns
# a list of (node, weight) edges. both of your graph implementations should be
# valid inputs. you may assume that the input graph is connected, and that all
# edges in the graph have positive edge weights.
#
# `source` and `target` are both nodes in the input graph. you may assume that
# at least one path exists from the source node to the target node.
#
# this method should return a tuple that looks like
# ([`source`, ..., `target`], `length`), where the first element is a list of
# nodes representing the shortest path from the source to the target (in
# order) and the second element is the length of that path
#
#note: Please see instructions.txt for additional information about the

#list of nodes which have subsequent neighbors (may not account for all nodes in Graph)
#Given a directed connected graph, t will be preceded by a node in Q

    def distance(node, d):
        if node in d:
            return d[node][1]
        else:
            return float("inf")

    Q = graph.get_outnodes()
    d[source] = ([source],0)


    u = source
    S.add(u)


    print('Initial Q: ',Q)
    print('Initial S: ',S)
    print('d',d)

    #if t is not found, stop iteration once all paths are Explored
    while len(Q) > 0:
        #Remove u after while check to permit one more rotation if t is not in Q [has no outnodes] and is preceded by the last node in Q
        Q.remove(u)
        print('Q is now: ',Q)
        print('S is now: ',S)

        print('distance(u)',distance(u,d))
        #returns list of [('neighbori',distancei)] tuples
        neighbors_weights = graph.get_neighbors(u)
        print('neighbors,weights of '+u+'-edges:',neighbors_weights)

        for v in neighbors_weights:
            #UPDATE d of all neighbors v of u, if distance to v is minimized via u
            print('v',v)
            if distance(u,d) + v[1] < distance(v[0],d):
                d[v[0]] = (d[u][0]+[v[0]],distance(u,d) + v[1])

        print('Distances:')
        print(d)


        #When min_key persists as t (t is minimum distance of unexplored nodes), found shortest path from s to t
        min_value = distance(target,d)
        print('starting min_val: ',min_value)
        min_key = target
        print('starting target: ',target)
        #Compare distances in d to distance(s,t)
        for key in d:
            print('key: ',key)
            if d[key][1] < min_value and key in Q and key not in S:
                min_value = d[key][1]
                min_key = key

            print('min_value is now:',min_value)
        print('min_key is now: ',min_key)
        #select key from Q and not S with shortest distance from s --> maintains invariant
        u = min_key

        if u == target:
            return d[u]
        S.add(u)

    return ([],float("inf"))

# YOUR CODE HERE
if __name__ == "__main__":
    # adjacency_graph is type dict
    _graph = AdjacencyGraph()
    print('AdjacencyGraph:')

    #edge_graph is type list
    # _graph = EdgeGraph()
    # print('EdgeGraph:')
    _graph.add_edge('s','2',9)
    _graph.add_edge('s','6',14)
    _graph.add_edge('s','7',15)
    _graph.add_edge('2','3',24)
    _graph.add_edge('6','3',18)
    _graph.add_edge('6','5',30)
    _graph.add_edge('6','7',5)
    _graph.add_edge('3','5',2)
    _graph.add_edge('3','t',19)
    _graph.add_edge('4','t',6)
    _graph.add_edge('4','3',6)
    _graph.add_edge('5','t',16)
    _graph.add_edge('5','4',11)
    _graph.add_edge('7','5',20)
    _graph.add_edge('7','t',44)

    print(_graph.graph)
    print('outnodes:')
    print(_graph.get_outnodes())
    print('shortest distance between s,t:',shortest_path(_graph,'s','t'))

    print('=============================================================')
    #edge_graph is type list
    _graph = EdgeGraph()
    print('EdgeGraph:')
    _graph.add_edge('s','2',9)
    _graph.add_edge('s','6',14)
    _graph.add_edge('s','7',15)
    _graph.add_edge('2','3',24)
    _graph.add_edge('6','3',18)
    _graph.add_edge('6','5',30)
    _graph.add_edge('6','7',5)
    _graph.add_edge('3','5',2)
    _graph.add_edge('3','t',19)
    _graph.add_edge('4','t',6)
    _graph.add_edge('4','3',6)
    _graph.add_edge('5','t',16)
    _graph.add_edge('5','4',11)
    _graph.add_edge('7','5',20)
    _graph.add_edge('7','t',44)

    print(_graph.graph)
    print('outnodes:')
    print(_graph.get_outnodes())

    print('shortest distance between s,t:',shortest_path(_graph,'s','t'))
