def can_choose(t, cases):
    results = []
 
    for n, m, k, a, b in cases:
        unique_a = set(a)
        unique_b = set(b)
 
        # Элементы, лежащие в пределах [1, k]
        relevant_a = {x for x in unique_a if x <= k}
        relevant_b = {x for x in unique_b if x <= k}
 
        only_a = relevant_a - relevant_b  # Элементы, встречающиеся только в a
        only_b = relevant_b - relevant_a  # Элементы, встречающиеся только в b
        both = relevant_a & relevant_b  # Элементы, встречающиеся в обоих
 
        # Проверка условий
        if len(only_a) > k // 2:
            results.append("NO")
            continue
 
        if len(only_b) > k // 2:
            results.append("NO")
            continue
 
        total_distinct = len(only_a) + len(only_b) + len(both)
        if total_distinct < k:
            results.append("NO")
            continue
 
        results.append("YES")
 
    return results
 
 
# Ввод данных
t = int(input())
cases = []
 
for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cases.append((n, m, k, a, b))
 
# Получение результатов
results = can_choose(t, cases)
 
# Вывод результатов
for result in results:
    print(result)