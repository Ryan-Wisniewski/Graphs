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
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Verticy does not exist.')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex. 
        bredth = across and queu
        The way I did it feels like cheating.
        """
        # Memo this ### Create a queue/stack as appropriate
        print('started BFT')
        queue = Queue()
        # put starting point in that 
        queue.enqueue(starting_vertex)
        #Make a set to keep track of where weve been ##### heh it was the first option nor did you pop anything. but good try.
        visited = set()
        #while there is stuff in the queue/stack
        print(queue.queue)
        while len(queue.queue) > 0:
        #   pop the first item
            vertex = queue.dequeue()
        #   if not visitied
            if vertex not in visited:
        #       DO THE THINGS!
                print('vertex',vertex)
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
        #           add that edge the queu/stack
                    queue.enqueue(next_vert)



        # ######## First attempt ish ####
        # current_vertex = self.vertices[starting_vertex]
        # # print('Start here: ', starting_vertex, current_vertex)
        # queue = Queue()
        # queue.enqueue(starting_vertex)
        # # print('queue', queue.queue)
        # for x in self.vertices:
        #     current_vertex = self.vertices[x]
        #     # print('yeet',x, current_vertex)
        #     for y in current_vertex:
        #         # print('CHECKHERE',x)
        #         if y not in queue.queue:
        #             print('not in queue', y)
        #             queue.enqueue(y)
        # print('final queue',queue.queue)

        # #now either set this queue to a empty array to dequeu and try again?
        # #or simply just return the one valid queu path. (but prob option 1)
        # heh it was the first option nor did you pop anything. but good try. ### and duh when you use the while loop dat was bett obv for runtime.. 
        pass
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex. depth = downward and stack
        """
        # Memo this ### Create a queue/stack as appropriate
        print('started DFT')
        stack = Stack()
        # put starting point in that 
        stack.push(starting_vertex)
        #Make a set to keep track of where weve been ##### heh it was the first option nor did you pop anything. but good try.
        visited = set()
        #while there is stuff in the queue/stack
        print(stack.stack)
        while len(stack.stack) > 0:
        #   pop the first item
            vertex = stack.pop()
        #   if not visitied
            if vertex not in visited:
        #       DO THE THINGS!
                print('vertex',vertex)
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
        #           add that edge the queu/stack
                    stack.push(next_vert)

        
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex):
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
    print('edge of graph',graph.vertices)

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
