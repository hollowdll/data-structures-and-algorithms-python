class Vertex:
    def __init__(self, value):
        self._value = value

    def __repr__(self):
        return f"<Vertex: {self._value}>"

    def __hash__(self):
        return hash(id(self))


class Edge:
    def __init__(self, u, v, x):
        self._first = u
        self._second = v
        self._value = x

    def __repr__(self):
        return f"<Edge ({self._value}): {self._first} --> {self._second}>"

    def endpoints(self):
        return (self._first, self._second)

    def opposite(self, v):
        return self._second if v is self._first else self._first

    def value(self):
        return self._value

    def __hash__(self):
        return hash((self._first, self._second))


class Graph:
    def __init__(self, adj_map=None):
        if adj_map:
            self._adj_map = adj_map
        else:
            self._adj_map = {}

    def get_vertices(self):
        return self._adj_map.keys()

    def get_edges(self):
        """Return a set of all edges of the graph."""
        result = set()
        for secondary_map in self._adj_map.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v) -> Edge | None:
        """
        Returns the edge from u to v, or None if not adjacents.
        """
        return self._adj_map[u].get(v)

    def degree(self, u):
        """
        Returns the number of edges incident to vertex u
        """
        return len(self._adj_map[u])

    def get_adjacent_vertices(self, u):
        """
        Return a list of the adjacent vertices of a given vertex
        """
        return list(self._adj_map[u].keys())

    def get_incident_edges(self, u):
        """
        Returns edges incident to vertex u
        """
        return list(self._adj_map[u].values())

    def add_vertex(self, value):
        vertex = Vertex(value)
        self._adj_map[vertex] = {}
        return vertex

    def add_edge(self, u, v, x=None):
        edge = Edge(u, v, x)
        self._adj_map[u][v] = edge
        self._adj_map[v][u] = edge

    def get_adj_map(self):
        return self._adj_map

    def get_adj_matrix(self):
        all_vertices = self._adj_map.keys()
        return [
            [int(bool(self._adj_map[u].get(v))) for v in all_vertices]
            for u in all_vertices
        ]