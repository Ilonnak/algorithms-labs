import heapq

def dijkstra(graph, start):
    # dist[v] – мінімальна відстань від start до v
    dist = {v: float('inf') for v in graph}
    dist[start] = 0

    # pred[v] – попередник у найкоротшому шляху
    pred = {v: None for v in graph}

    pq = [(0, start)]  # черга з пріоритетом (distance, vertex)

    while pq:
        current_dist, u = heapq.heappop(pq)

        # Якщо отримано застаріле значення — пропускаємо
        if current_dist > dist[u]:
            continue

        # Переглядаємо всіх сусідів
        for v, weight in graph[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                pred[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, pred


def restore_path(pred, start, end):
    """Відновлення шляху назад"""
    path = []
    v = end
    while v is not None:
        path.append(v)
        v = pred[v]
    path.reverse()

    if path[0] != start:
        return None
    return path


graph = {
    1: [(3, 1), (2, 4), (4, 4)],
    2: [(1, 4), (3, 5), (6, 3), (5, 7)],
    3: [(1, 1), (2, 5), (6, 5), (8, 4)],
    4: [(1, 4), (2, 5), (5, 1)],
    5: [(4, 1), (2, 7), (7, 4)],
    6: [(2, 3), (3, 5), (7, 6)],
    7: [(5, 4), (6, 6), (8, 5)],
    8: [(3, 4), (7, 5)]
}

start_vertex = 1

dist, pred = dijkstra(graph, start_vertex)

print("Найкоротші відстані від вершини", start_vertex)
for v in graph:
    print(f"{start_vertex} → {v}: dist = {dist[v]}")

print("\nШляхи:")
for v in graph:
    if v != start_vertex:
        path = restore_path(pred, start_vertex, v)
        print(f"{start_vertex} → {v}: шлях = {path}, вага = {dist[v]}")

