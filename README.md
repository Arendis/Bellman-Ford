# Bellman-Ford
В написанном алгоритме явно выделяется часть, которая может быть распараллелена – вложенный цикл, 
проходящий по всем граням. Значение каждой итерации данного цикла не зависит от значения предыдущей, 
соответственно, их можно выполнять не последовательно, а в параллель. 

# находим растояния
# for i in range(1,len(graph)):\
## вот здесь
# for u,v,w in edges:
## if dist[u] + w < dist[v]:
### dist[v] = dist[u] + w

