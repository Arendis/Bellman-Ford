
# Алгоритм Беллмана-Форда

# Алгоритм взят с https://github.com/mtn/icpc-cuddly-happiness/blob/a25bf69bb979859a3b67cf7b2a7eb909648f86a4/importantAlgs.py

# импортируем библиотеку времени, для того, чтобы засечь сколько работала программа
import threading
import time

graph = {0: {1: 10, 5: 8},
         1: {3: 1},
         2: {1: 1},
         3: {2: -2},
         4: {1: -4, 3: -1},
         5: {4: 1}}

def graph1(a,b,c,d,f,g,k,l):
    graph = {0: {1: a, 5: b},
             1: {3: c},
             2: {1: d},
             3: {2: f},
             4: {1: g, 3: k},
             5: {4: l}}
    return graph


start = time.time()

def BellmanFord(graph,source):
    dist = {}; prev = {}; edges = []
    for u in graph:
        dist[u] = float('inf')
        prev[u] = None
        edges += [(u,v,weight) for v,weight in graph[u].items()]
    dist[source] = 0
    # находим растояния
    for i in range(1,len(graph)):
        #распараллеливать тут
        for u,v,w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    # Проверка на наличие циклов отрицательного веса
    for u,v,w in edges:
        assert dist[u] + w >= dist[v], 'цикл отрицательного веса'
    print('Вершина {}: '.format(source), dist)
    #time.sleep(5) # убеждаемся что потоки запустились одновреммено
    return dist

# тестирование
if __name__ == "__main__":
    #print('Вершина: 0')
    #print(BellmanFord(graph, 3))
    thread_list = []
    for i in range(6):
        t = threading.Thread(target=BellmanFord, name= i, args=(graph, i))
        t.start()
    for t in thread_list:
        t.join()


