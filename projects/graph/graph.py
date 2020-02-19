"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {
            # "A": set("B", "C", "D"),
            # "B": set(),
            # "C": set(),
            # "D": set() 
        }

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    #BREADTH FIRST TRAVERSAL
    def bft(self, starting_vertex): 
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Make a queue
        queue = Queue()
        # Make a set for the visited nodes
        visited = set()

        # Put our starting node in line
        queue.enqueue(starting_vertex)

        # If our queue is not yet empty, we have more people to visit
        while queue.size() > 0:
            # Get the next node out of line
            current_node = queue.dequeue()

            # Check is it has been visited
            if current_node not in visited:
            ## if not, mark as visited
                visited.add(current_node)
                print(current_node)
            ## and get it's neighbors
                edges = self.get_neighbors(current_node)
            ## put them in line to be visited
                for edge in edges:#self.vertices[current_node]:
                    queue.enqueue(edge)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Make a stack
        stack = Stack()
        # Make a set for the visited nodes
        visited = set()

        # Put our starting node on top of stack
        stack.push(starting_vertex)

        # If our stack is not yet empty, we have more people to visit
        while stack.size() > 0:
            # Get the next node off the top of the stack
            current_node = stack.pop()

            # Check is it has been visited
            if current_node not in visited:
            ## if not, mark as visited
                visited.add(current_node)
                print(current_node)
            ## and get it's neighbors
                edges = self.get_neighbors(current_node)
            ## push them to stack to be visited
                for edge in edges:
                    stack.push(edge)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        visited.add(starting_vertex)
        
        edges = self.get_neighbors(starting_vertex)

        if len(edges) == 0:
            return

        for edge in edges:
            if edge not in visited:
                self.dft_recursive(edge, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # BREADTH-FIRST SEARCH
        # MAKE A QUEUE
        queue = Queue()
        # MAKE A SET FOR VISITED
        visited = set()

        # ENQUEUE A PATH TO THE STARTING_VERTEX
        queue.enqueue([starting_vertex])

        # WHILE THE QUEUE ISN'T EMPTY:
        while queue.size() > 0:
            ## DEQUEUE THE NEXT PATH
            current_path = queue.dequeue()
            ## CURRENT_NODE IS THE LAST THING IN THE PATH
            current_node = current_path[-1]

            ## CHECK IF IT'S THE TARGET, AKA THE DESTINATION_VERTEX
            if current_node == destination_vertex:
                ## IF SO, RETURN THE PATH
                return current_path

            else:
                ## IF NOT, MARK THIS AS VISITED
                if current_node not in visited:
                    visited.add(current_node)
                    ## GET THE NEIGHBORS
                    edges = self.get_neighbors(current_node)

                    for edge in edges:
                         ## COPY THE PATH, ADD THE NEIGHBOR TO THE COPY
                        path_copy = list(current_path)
                        path_copy.append(edge)
                        ## FOR EACH ONE, ADD A PATH TO IT IN OUR QUEUE
                        queue.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # MAKE A STACK
        stack = Stack()
        # MAKE A SET FOR VISITED
        visited = set()

        # PUSH A PATH TO THE STARTING_VERTEX
        stack.push([starting_vertex])

        # WHILE THE STACK ISN'T EMPTY:
        while stack.size() > 0:
            ## POP THE NEXT PATH
            current_path = stack.pop()
            ## CURRENT_NODE IS THE LAST THING IN THE PATH
            current_node = current_path[-1]

            ## CHECK IF IT'S THE TARGET, AKA THE DESTINATION_VERTEX
            if current_node == destination_vertex:
                ## IF SO, RETURN THE PATH
                return current_path

            else:
                ## IF NOT, MARK THIS AS VISITED
                if current_node not in visited:
                    visited.add(current_node)
                    ## GET THE NEIGHBORS
                    edges = self.get_neighbors(current_node)

                    for edge in edges:
                         ## COPY THE PATH, ADD THE NEIGHBOR TO THE COPY
                        path_copy = list(current_path)
                        path_copy.append(edge)
                        ## FOR EACH ONE, ADD A PATH TO IT IN OUR STACK
                        stack.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()

        visited.add(starting_vertex)
        
        edges = self.get_neighbors(starting_vertex)

        if len(edges) == 0:
            return

        for edge in edges:
            if edge not in visited:
                self.dft_recursive(edge, visited)

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
    print(graph.bfs(1, 4))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
