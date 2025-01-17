def solve(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    sum = 0
    for i in range(1, n+1):
        sum += i * (2 * i - 1)
    ops = 2 * n
    for i in range(n-1, -1, -1):
        matrix[i] = list(range(1, n+1))  
        for j in range(n):
            matrix[j][i] = j + 1  
    print(sum, ops)
    for i in range(n, 0, -1):
        for j in range(1, 3):
            print(j, i, end=' ')  
            for k in range(1, n+1):
                print(k, end=' ')  
            print() 


    

def main():
    for _ in range(int(input())):
        n=int(input())
        solve(n)


main()