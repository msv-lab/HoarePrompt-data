def func_1(no, grafo, visitados, depth, cand):
    if no[1]:
        cand['value'] = max(cand['value'], no[0])
    visitados[no[0]] = True
    for vizinho in grafo[no[0]]:
        if not visitados[vizinho[0]]:
            func_1(vizinho, grafo, visitados, depth + 1, cand)
n = int(raw_input())
grafo = [[] for _ in xrange(n + 1)]
for i in xrange(1, n):
    (a, b, t) = map(int, raw_input().split())
    grafo[a].append((b, False if t == 1 else True))
    grafo[b].append((a, False if t == 1 else True))
visitados = [False for _ in xrange(n + 1)]
vizinhos = grafo[1]
visitados[1] = True
candi = []
for vizinho in vizinhos:
    maxi = {'value': -1}
    func_1(vizinho, grafo, visitados, 1, maxi)
    if maxi['value'] != -1:
        candi.append(maxi['value'])
print(len(set(candi)))
print(' '.join(list(set(map(str, candi)))))