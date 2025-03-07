from collections import Counter
 
nabors = int(input())
for _ in range(nabors):
    # цикл по наборам данных ----------------
    
    # в каждом наборе получаем по две строки
    # 1)  три целых числа n, m и k
    n, m, k = [int(i) for i in input().split()]
    
    # 2) элементы массива a
    aa = [int(i) for i in input().split()]
 
    # 3) элементы массива b
    bb = [int(i) for i in input().split()]
    
    cnt_aa = Counter(aa[:m])  
    cnt_bb = Counter(bb)
    D = cnt_aa & cnt_bb  # D -найденные парные совпадения в cnt_aa и cnt_bb
    E = cnt_aa - D       # E - несовпавшие элементы из cnt_aa
    C = cnt_bb - D       # C - несовпавшие элементы из cnt_bb
    
    tot = sum(D.values())
    fnd = 1 if tot >= k else 0
    
    for in_aa,out_aa in zip(aa[m:], aa[:n-m]):
        if D[out_aa] > 0:
            if E[out_aa] > 0:
                E[out_aa] -= 1
            else:
                D[out_aa] -= 1
                C[out_aa] += 1
        else:
            E[out_aa] -= 1
            
        if C[in_aa] > 0:
            # случай, когда возможно ранее уже есть такая пара
            if C[in_aa] == D[in_aa]:
                C[in_aa] += 1
            else:
                D[in_aa] += 1
        else:
            E[in_aa] += 1
        tot = sum(D.values())
        fnd += 1 if tot >= k else 0    
    
    print(fnd)