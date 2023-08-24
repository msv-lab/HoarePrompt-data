T = int(input())
N = int(input())
monkeys_first_type = []
for _ in range(N):
    A, B = map(int, input().split())
    monkeys_first_type.append((A, B))
M = int(input())
monkeys_second_type = []
for _ in range(M):
    C, D = map(int, input().split())
    monkeys_second_type.append((C, D))

min_time_first_type = min([A + (T - A) // B * B for A, B in monkeys_first_type])
max_time_first_type = max([(A + (T - A) // B * B) + (T - A) % B for A, B in monkeys_first_type])

min_time_second_type = min([C + (T - C) // D * D for C, D in monkeys_second_type])
max_time_second_type = max([(C + (T - C) // D * D) + (T - C) % D for C, D in monkeys_second_type])

first_type_arrival = max(min_time_first_type, min_time_second_type)
second_type_arrival = min(max_time_first_type, max_time_second_type)

result = second_type_arrival - first_type_arrival
print(result)