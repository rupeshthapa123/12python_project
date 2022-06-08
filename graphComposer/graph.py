import random

# The Vertex class is a node in the graph. It has a value, a dictionary of adjacent vertices, and a
# list of neighbors and their weights
class Vertex:
    def __init__(self, value):
        """
        The function takes in a value and creates a node with that value
        
        :param value: The value of the node
        """
        self.value = value
        self.adjacent = {}
        self.neighbors = []
        self.neighbors_weights = []

    def add_edge_to(self, vertex, weight=0):
        """
        This function adds a vertex to the adjacency list of the current vertex
        
        :param vertex: The vertex to add an edge to
        :param weight: The weight of the edge between the two vertices, defaults to 0 (optional)
        """
        self.adjacent[vertex] = weight
    
    def increment_edge(self, vertex):
        """
        If the vertex is already in the dictionary, increment the value by 1. Otherwise, add the vertex
        to the dictionary with a value of 1
        
        :param vertex: The vertex to increment the edge count for
        """
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1
    
    def get_probability_map(self):
        """
        It takes the adjacent vertices and weights of a vertex and adds them to the vertex's neighbors
        and neighbors_weights lists.
        """
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)
        
    def next_word(self):
        """
        > Given a list of neighbors and a list of weights, return a random neighbor based on the weights
        :return: A random word from the list of neighbors.
        """
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]

# The Graph class is a container for all the vertices in the graph. It has methods for adding
# vertices, getting vertices, and getting the next word in the graph
class Graph:
    def __init__(self):
        """
        The function __init__() is a special function in Python classes. It is run as soon as an object
        of a class is instantiated. The method is useful to do any initialization you want to do with
        your object
        """
        self.vertices = {}

    def get_vertex_values(self):
        """
        It returns a set of all the vertex values in the graph
        :return: The keys of the vertices dictionary.
        """
        return set(self.vertices.keys())
    
    def add_vertex(self, value):
        """
        We create a new key in the vertices dictionary with the value of the vertex as the key and the
        vertex object as the value
        
        :param value: The value of the vertex to be added
        """
        self.vertices[value] = Vertex(value)
    
    def get_vertex(self, value):
        """
        If the value is not in the graph, add it. Then return the vertex
        
        :param value: The value of the vertex to get
        :return: The vertex with the value that is passed in.
        """
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]
    
    def get_next_word(self, current_vertex):
        """
        Given a vertex, return the next word in the graph
        
        :param current_vertex: The current vertex we're at in the graph
        :return: The next word in the graph.
        """
        return self.vertices[current_vertex.value].next_word()
    
    def generate_probability_mappings(self):
        """
        For each vertex in the graph, generate a probability map that maps each vertex to a probability
        of being the next vertex in the graph.
        """
        for vertex in self.vertices.values():
            vertex.get_probability_map()

