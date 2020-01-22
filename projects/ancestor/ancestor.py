import os
import sys
sys.path.append('../graph')
from graph import Graph
def earliest_ancestor(ancestors, starting_node):
    # 1 answer 1 solution 1 start 
    # the data even looks like it wants to traverse in a column like pattern
    #DFT FTW #### UPDATE ITS DA REVERSE DOE. I see.
    # Traversal not search beacause we wana always wana explore all the way to the end of the list
    graph = Graph()
    for i in range(1, 12):
        graph.add_vertex(i)
    for i in range(len(ancestors)):
        #bwahaha it really was as easy as flipping theese.
        graph.add_edge(ancestors[i][1], ancestors[i][0])
    if graph.dft(starting_node) == starting_node:
        return -1
    
    return graph.dft(starting_node)

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 1)











# # Memo this ### Create a stack as appropriate
#     print('started DFT for greatest ancestor')
#     stack = Stack()
#     # put starting point in that 
#     stack.push(starting_node)
#     #Make a set to keep track of where weve been
#     visited = set()
#     #while there is stuff in the stack
#     while stack.size() > 0:
#         # pop the first item
#         vertex = stack.pop()
#         # if not visitied
#         if vertex not in visited:
#             # DO THE THINGS!
#             print(vertex)
#             visited.add(vertex)
#             #For each edge in the item
#             for next_vert in ancestors:
#                 # add that edge the queu/stack
#                 stack.push(next_vert)