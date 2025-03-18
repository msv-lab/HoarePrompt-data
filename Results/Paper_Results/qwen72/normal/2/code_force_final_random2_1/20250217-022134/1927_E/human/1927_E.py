# https://codeforces.com/problemset/problem/1927/E
 
 
def case():
    n,k = map(int,input().split(" "))
 
    permutation = [0] * n
 
    idx = 0
    idx_v = 1
 
    curr_v = 1
    for i in range(k):
        multiples_of_k_plus_i = i
        while multiples_of_k_plus_i < len(permutation):
            permutation[multiples_of_k_plus_i] = curr_v
            curr_v += 1
            multiples_of_k_plus_i += k
 
    result = " ".join([str(v) for v in permutation])
    print(result)
 
 
def main():
    t = int(input())
    while t > 0:
        case()
        t -= 1
 
if __name__ == "__main__":
    main()