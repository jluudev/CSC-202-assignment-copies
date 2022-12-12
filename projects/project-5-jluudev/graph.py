from typing import Any, List, Optional
from stack_array import *  # Needed for Depth First Search
from queue_array import *  # Needed for Breadth First Search


class Vertex:
    '''Add additional helper methods if necessary.'''

    def __init__(self, key: Any):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to: List = []
        self.color: int = -1


class Graph:
    '''Add additional helper methods if necessary.'''

    def __init__(self, filename: str):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified
           in the input file should appear on the adjacency list of each vertex of the two vertices associated
           with the edge.'''
        self.graph: dict = {}

        with open(filename, "r") as file:
            for line in file:
                l = line.split()
                self.add_vertex(l[0])
                self.add_vertex(l[1])
                self.add_edge(l[0], l[1])
            file.close()

    def add_vertex(self, key: Any) -> None:
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if key not in self.graph:
            self.graph[key] = Vertex(key)

    def get_vertex(self, key: Any) -> Optional[Vertex]:
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        if key not in self.graph:
            return None
        return self.graph[key]

    def add_edge(self, v1: Any, v2: Any) -> None:
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        if v2 not in self.graph[v1].adjacent_to:
            self.graph[v1].adjacent_to.append(v2)
        if v1 not in self.graph[v2].adjacent_to:
            self.graph[v2].adjacent_to.append(v1)

    def get_vertices(self) -> List:
        '''Returns a list of id's representing the vertices in the graph, in ascending order
           Note: Results of Python sort on the list satisifies ascending order requirement'''

        key_list = list(self.graph.keys())
        key_list.sort()
        return key_list


    def conn_components(self) -> List:
        '''Returns a list of lists.  For example, if there are three connected components
           then you will return a list of three lists.  Each sub list should contain the
           vertices (in 'Python List Sort' order) in the connected component represented by that list.
           The overall list of lists should also be in order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        stack = Stack(len(self.graph))
        keys = list(self.graph.keys())
        sublist: List = []
        ret_list: List = []

        while len(keys) != 0:
            stack.push(keys[0])

            while not stack.is_empty():
                cur_key = stack.pop()
                cur_v = self.get_vertex(cur_key)
                if cur_v:
                    adj = cur_v.adjacent_to

                for v in adj:
                    if v not in sublist:
                        stack.push(v)

                if cur_key not in sublist:
                    sublist.append(cur_key)

            for k in sublist:
                if k in keys:
                    keys.remove(k)

            sublist.sort()
            ret_list.append(sublist)
            sublist = []

        return ret_list

    def is_bipartite(self) -> bool:
        '''Returns True if the graph is bicolorable and False otherwise.
        This method MUST use Breadth First Search logic!'''
        comp = self.conn_components()
        #print(comp)
        q = Queue(len(self.get_vertices()))
        for sub in comp:
            v = sub[0]
            self.graph[v].color = 1
            q.enqueue(v)
            while not q.is_empty():
                cur = q.dequeue()
                for i in self.graph[cur].adjacent_to:
                    if self.graph[cur].color == 1 and self.graph[i].color == -1:
                        self.graph[i].color = 1 - self.graph[cur].color
                        q.enqueue(i)

                    elif self.graph[cur].color == self.graph[i].color:
                        return False
        return True





