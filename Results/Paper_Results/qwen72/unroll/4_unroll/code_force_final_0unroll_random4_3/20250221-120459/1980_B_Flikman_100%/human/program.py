t = int(input())
 
for _ in range(t):
    # Чтение входных данных
    n, f, k = map(int, input().split())
    a = list(map(int, input().split()))
 
    # Значение любимого кубика
    favorite_value = a[f - 1]
 
    # Сортируем кубики по невозрастанию значений
    sorted_a = sorted(a, reverse=True)
 
    # Подсчёт индекса любимого кубика в отсортированном массиве
    removed_count = 0
    for i in range(k):
        if sorted_a[i] == favorite_value:
            removed_count += 1
 
    # Подсчитываем количество одинаковых любимому кубику
    favorite_count = sorted_a.count(favorite_value)
 
    # Определяем, удалён ли любимый кубик
    if removed_count == favorite_count:
        print("YES")
    elif removed_count == 0:
        print("NO")
    else:
        print("MAYBE")