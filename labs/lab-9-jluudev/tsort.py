from stack_array import *


class Vertex:
    def __init__(self, adjacencies: List):
        self.in_degree = 0
        self.adjacencies = adjacencies


def tsort(vertices: List) -> str:
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility {@code tsort}.  That is, one vertex per
    * line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''

    if len(vertices) == 0:
        raise ValueError("input contains no edges")

    if len(vertices) % 2 == 1:
        raise ValueError("input contains an odd number of tokens")

    str_output = ""
    vertex_ord = []
    adj_dict = {}
    zero_stack = Stack(len(vertices))

    for index, i in enumerate(vertices):
        if i not in adj_dict:
            vertex_ord.append(i)
            adj_dict[i] = Vertex([])
        if index % 2 == 1:
            adj_dict[i].in_degree += 1
            adj_dict[vertices[index-1]].adjacencies.append(i)

    for i in vertex_ord:
        if adj_dict[i].in_degree == 0:
            zero_stack.push(i)

    if zero_stack.is_empty():
        raise ValueError("input contains a cycle")

    while not zero_stack.is_empty():
        popped = zero_stack.pop()
        str_output = str_output + popped + "\n"
        for j in adj_dict[popped].adjacencies:
            adj_dict[j].in_degree -= 1

            if adj_dict[j].in_degree == 0:
                zero_stack.push(j)

        adj_dict.pop(popped)

    if len(adj_dict) != 0:
        raise ValueError("input contains a cycle")

    return str_output
