def find_path(n, routers):
    path = [1]
    for i in range(2, n+1):
        router = routers[i-2]
        if router in path:
            index = path.index(router)
            path = path[:index] + [i]
        else:
            path.append(i)
    return path

n = int(input())
routers = list(map(int, input().split()))

path = find_path(n, routers)
print(" ".join(map(str, path)))