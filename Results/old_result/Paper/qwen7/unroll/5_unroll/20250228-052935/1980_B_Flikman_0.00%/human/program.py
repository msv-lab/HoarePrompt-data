t = int(input())
 
for _ in range(t):
    # Чтение входных данных
    n, f, k = map(int, input().split())
    a = list(map(int, input().split()))
 
    # Значение любимого кубика
    favorite_value = a[f - 1]
 
    # Подсчет количества кубиков с таким же значением
    same_value_count = 0
    for value in a:
        if value == favorite_value:
            same_value_count += 1
 
    # Подсчет количества кубиков, у которых значения больше любимого
    greater_count = 0
    for value in a:
        if value > favorite_value:
            greater_count += 1
 
    # Проверка условий удаления любимого кубика
    if greater_count >= k:
        print("YES")
    elif greater_count + same_value_count <= k:
        print("NO")
    else:
        print("MAYBE")