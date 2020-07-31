from graph import Graph
def earliest_ancestor(ancestors, starting_node):
    #create graph structure to hold and query ancestors
    family_graph = Graph()
    #iterate of each family pair adding them to graph
    #then adding the edges
    for family in ancestors:
        family_graph.add_vertex(family[0])
        print(f"Parent {family[0]} added")
        family_graph.add_vertex(family[1])
        print(f"Child of {family[0]}, {family[1]} added")
        family_graph.add_edge(family[0],family[1])
        print(f'Edge added between {family[0]} and {family[1]}')
    for i in family_graph.get_neighbors(1):
        print(i)

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors,0)