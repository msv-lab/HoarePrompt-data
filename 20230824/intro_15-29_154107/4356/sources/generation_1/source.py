# Read inputs
N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

# Check if template image B is contained in image A
def check_containment(A, B):
    # Iterate through each starting position in image A
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            found = True
            # Compare template image B with subimage of A
            for x in range(M):
                for y in range(M):
                    if A[i + x][j + y] != B[x][y]:
                        found = False
                        break
                if not found:
                    break
            if found:
                return True
    return False

# Check containment and print result
if check_containment(A, B):
    print("Yes")
else:
    print("No")