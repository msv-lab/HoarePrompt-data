from collections import Counter
 
nabors = int(input())
for _ in range(nabors):
    # цикл по наборам данных ----------------
    
    # в каждом наборе получаем по две строки
    # 1)  три целых числа n, m и k
    n, m, k = [int(i) for i in input().split()]
    
    # 2) элементы массива a
    aa = [str(i) for i in input().split()]
 
    # 3) элементы массива b
    bb = [str(i) for i in input().split()]
    
    cnt_aa = Counter(aa[:m])  
    cnt_bb = Counter(bb)
    D = cnt_aa & cnt_bb  # D -найденные парные совпадения в cnt_aa и cnt_bb
    pairs_in_D = sum(D.values())  # сколько пар в D
    
    E = cnt_aa - D       # E - несовпавшие элементы из cnt_aa
    C = cnt_bb - D       # C - несовпавшие элементы из cnt_bb
    
    fnd = 1 if pairs_in_D >= k else 0
    
    for in_aa,out_aa in zip(aa[m:], aa[:n-m]):
        if D[out_aa] > 0:
            if E[out_aa] > 0:
                E[out_aa] -= 1
            else:
                D[out_aa] -= 1
                pairs_in_D -= 1 
                C[out_aa] += 1
        else:
            E[out_aa] -= 1
            
        if C[in_aa] > 0:
            # случай, когда возможно ранее уже есть такая пара
            D[in_aa] += 1
            pairs_in_D += 1 
            C[in_aa] -= 1
        else:
            E[in_aa] += 1
            
        fnd += 1 if pairs_in_D >= k else 0  
    
    print(fnd)