def min_problems_to_create():
    t = int(input())
    results = []
    required_problems = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
    
    for _ in range(t):
        n, m = map(int, input().split())
        a = input().strip()
        
        # Подсчёт задач в банке
        problem_count = {}
        for ch in a:
            if ch in problem_count:
                problem_count[ch] += 1
            else:
                problem_count[ch] = 1
        
        # Подсчёт недостающих задач
        missing_problems = 0
        for p in required_problems:
            if p not in problem_count or problem_count[p] < m:
                missing_problems += m - problem_count.get(p, 0)
        
        results.append(missing_problems)
    
    for res in results:
        print(res)

# Запуск программы
min_problems_to_create()