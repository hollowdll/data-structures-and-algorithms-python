from graph import Vertex, Edge, Graph, DFS

def main():
    A = Vertex('A')
    B = Vertex('B')
    C = Vertex('C')
    D = Vertex('D')
    E = Vertex('E')
    F = Vertex('F')

    AB = Edge(A, B, 2)
    AC = Edge(A, C, 4)
    BD = Edge(B, D, 5)
    CD = Edge(C, D, 9)
    CE = Edge(C, E, 3)
    DF = Edge(D, F, 2)
    EF = Edge(E, F, 2)

    adj_map = {
        A: { B: AB, C: AC },
        B: { A: AB, D: BD }, 
        C: { A: AC, D: CD, E: CE },
        D: {B: BD, C: CD, F: DF},
        E: {C: CE, F: EF},
        F: {D: DF, E: EF}
    }

    g = Graph(adj_map)
    print(DFS(g, A))
    # {<Vertex: A>: None, <Vertex: B>: <Vertex: A>, <Vertex: D>: <Vertex: B>,
    # <Vertex: C>: <Vertex: D>, <Vertex: E>: <Vertex: C>, <Vertex: F>: <Vertex: E>}

if __name__ == '__main__':
    main()