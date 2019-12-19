
# Алгоритм Беллмана-Форда

# Алгоритм взят с https://github.com/mtn/icpc-cuddly-happiness/blob/a25bf69bb979859a3b67cf7b2a7eb909648f86a4/importantAlgs.py

# импортируем библиотеку времени, для того, чтобы засечь сколько работала программа
import time

graph = {0: {1: -2},
         1: {2: -1},
         2: {0: 4, 3: 2, 4: -3},
         3: {},
         4: {},
         5: {0: -1, 3: 1, 4: -4}}

def graph1(a,b,c,d,f,g):
    graph  = {
        0:{1:a,2:b},
        1:{2:c,0:d},
        2:{0:f,1:g}}
    return graph


start = time.time()

def BellmanFord(graph,source):
    """
    Input:  Dictionary { node : {neighbor:weight} }
    Output: Dictionaries: distance
    """
    dist = {}; prev = {}; edges = []
    for u in graph:
        dist[u] = float('inf')
        prev[u] = None
        edges += [(u,v,weight) for v,weight in graph[u].items()]
    dist[source] = 0

    # находим растояния
    for i in range(1,len(graph)):
        for u,v,w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Проверка на наличие циклов отрицательного веса
    for u,v,w in edges:
        assert dist[u] + w >= dist[v], 'цикл отрицательного веса'
    return dist

# тестирование
if __name__ == "__main__":
    print('Вершина: 0')
    print(BellmanFord(graph, 0))

    print('Вершина: 1')
    print(BellmanFord(graph1(9,8,-1,1,1,2), 1))

