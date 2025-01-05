for _ in range(int(input())):
    l = list(map(int, input().split()))
    dis = list(map(int, input().split()))
    tmp = list(map(int, input().split()))

    # Vérification si les listes sont déjà triées ou si elles nécessitent des ajustements
    if dis[0] != 0:
        dis.insert(0, 0)
    if tmp[0] != 0:
        tmp.insert(0, 0)

    unit = []
    for i in range(1, len(dis)):
        unit.append((dis[i] - dis[i-1]) / (tmp[i] - tmp[i-1]))

    queries = [int(input()) for _ in range(l[2])]
    
    results = []
    for q in queries:
        if q == 0:
            results.append(0)
            continue
        
        total_time = 0.0
        for i in range(1, len(dis)):
            if dis[i-1] < q <= dis[i]:
                total_time += (q - dis[i-1]) / unit[i-1]
                break
            total_time += (dis[i] - dis[i-1]) / unit[i-1]
        
        results.append(int(total_time))
    
    for result in results:
        print(result)


 