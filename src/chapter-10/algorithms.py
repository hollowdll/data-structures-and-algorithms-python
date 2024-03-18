from graph import Vertex, Edge, Graph

def merge_sort(array):
    """
    Sort the array using the Merge sort algorithm
    
    Parameters:
    - array: The array to be sorted
    
    Returns: The sorted array.
    """

    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    merged_array = []
    left_index = right_index = 0

    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    # loop the halves and compare the values
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            merged_array.append(left_half[left_index])
            left_index += 1
        else:
            merged_array.append(right_half[right_index])
            right_index += 1

    # add the remaining elements of the other half
    if left_index < len(left_half):
        merged_array.extend(left_half[left_index:])
    elif right_index < len(right_half):
        merged_array.extend(right_half[right_index:])

    return merged_array

def fib(n):
    """
    Calculate the Fibonacci's series value for integer n.
    This solution uses tabulation to calculate the result bottom-up.
    
    Parameters:
    - n: The number to use in the Fibonacci's series.
    
    Returns: The calculated value of the Fibonacci's series for n
    """
    if n < 2:
        return 1

    a = 1   # n - 1
    b = 1   # n - 2

    for _ in range(n-1):
        result = a + b
        a, b = result, a

    return result

def dijkstra_shortest_path(source_vertex: Vertex, destination_vertex: Vertex, graph: Graph):
    """
    Calculate the shortest past (in distance value) between given vertices
    
    Parameters:
    - source_vertex: The source vertex
    - destination_vertex: The destination vertex
    - graph: The graph in question
    
    Returns: a tuple containing the minimum distance between vertices and a list of
             vertices that form the minimum path from one vertex to the other.
    """
    unvisited_vertices = graph.get_vertices()
    shortest_paths = { vertex: {'shortest': float('inf'), 'previous': None} for vertex in unvisited_vertices }
    # source has distance 0
    shortest_paths[source_vertex]['shortest'] = 0

    while unvisited_vertices:
        current_vertex = min(unvisited_vertices, key=lambda vertex: shortest_paths[vertex]['shortest'])
        distance_from_source = shortest_paths[current_vertex]['shortest']
        unvisited_adj_vertices = (v for v in graph.get_adjacent_vertices(current_vertex) if v in unvisited_vertices)

        for adj_vertex in unvisited_adj_vertices:
            edge = graph.get_edge(current_vertex, adj_vertex)
            # distance from source to this vertex
            total_distance = distance_from_source + edge.value()

            if total_distance < shortest_paths[adj_vertex]['shortest']:
                shortest_paths[adj_vertex]['shortest'] = total_distance
                shortest_paths[adj_vertex]['previous'] = current_vertex

        unvisited_vertices.remove(current_vertex)

    path = []
    current_vertex = destination_vertex

    while current_vertex:
        path.append(current_vertex)
        current_vertex = shortest_paths[current_vertex]['previous']

    return (shortest_paths[destination_vertex]['shortest'], path[::-1])
