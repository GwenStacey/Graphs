"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        # enqueue our first node
        queue = Queue()
        queue.enqueue(starting_vertex)
        # make a set to track visited nodes
        visited = set()
        # while queue still has items
        while queue.size()>0:
            ## dequeue from front of line, that is current node
            current_node = queue.dequeue()
            ##Check if visited
            if current_node not in visited:
                ###Mark as visited
                visited.add(current_node)
                print(current_node)
                ###Get neighbors
                neighbors = self.get_neighbors(current_node)
                ###Iterate over neighbors
                for neighbor in neighbors:
                    ###Add to queue
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #Make a stack, add the first node
        stack = Stack()
        stack.push(starting_vertex)
        #Make a set to track visited nodes
        visited = set()
        #As long as stack isn't empty
        ##Pop top, set to current node
        while stack.size()>0:
            current_node = stack.pop()
            ##Check if visited, if not:
            ###Add to visited
            if current_node not in visited:
                visited.add(current_node)
                print(current_node)
                ###Get neighbors
                neighbors = self.get_neighbors(current_node)
                ###Iterate over neighbors
                for neighbor in neighbors:
                    ###Add to stack
                    stack.push(neighbor)

    #Base Case
    # Progress towards the case by calling itself

    def dft_recursive(self, vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()
        #Check if visited
        if vertex not in visited:
            visited.add(vertex)
            neighbors = self.get_neighbors(vertex)
            #Base case is if no neighbors
            if len(neighbors) == 0:
                return visited
            #If we do have neighbors, iterate over them and recurse for each one
            for neighbor in neighbors:
                self.dft_recursive(neighbor, visited)
            
        

    def bfs(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #Make a queue
        queue = Queue()
        #Make a data structure to track visited
        if visited == None:
            visited = set()
        #Enqueue a PATH TO the starting vertex
        path = [starting_vertex]
        queue.enqueue(path)
        ##As long as queue isn't empty
        while queue.size() > 0:
        ###Dequeue from the front of the line
            current_path = queue.dequeue()
        ### current_node is the last thing in the path
            current_node = current_path[-1]
        ###Check if this is target node
            if current_node == destination_vertex:
        ####If so return
                return current_path
        ####Check if visited, if not:
        ####Mark as visited
        if current_node not in visited:
            visited.add(current_node)
        ####Get the current node's neighbor
            neighbors = self.get_neighbors(current_node)
        ####iterate over the neighbors
            for neighbor in neighbors:
        ####Add neighbors to path
                neighbor_path = current_path.copy()
                neighbor_path.append(neighbor)
        ####Enqueue neighbors path
                queue.enqueue(neighbor_path)
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
