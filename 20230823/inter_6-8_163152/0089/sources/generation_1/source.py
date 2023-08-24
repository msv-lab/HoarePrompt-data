def minimal_layers(N):
    return int(N*(N+1)*(N+2)/6)

N = int(input())
print(minimal_layers(N))