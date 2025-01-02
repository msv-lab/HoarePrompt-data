'''
Created on Feb 5, 2015

@author: simonm
'''
from fractions import gcd
import sys
from heapq import heappush, heappop

def set_gcd(numbers):
    ret = 0
    for number in numbers:
        ret = gcd(ret, number)
    return ret
    
# solution = (cost, set(cards))
# def solve(solution, cards, costs):
#     # base case
#     if set_gcd(solution[1]) == 1 : return solution[0]
#     # look for the result recursively
#     result = -1    
#     for cost, card in zip(costs, cards):
#         if card not in solution[1] :
#             s = solve((solution[0] + cost, solution[1].union([card])), cards, costs)
#             if result == -1 : result = s
#             elif s != -1 and s < result : result = s
#     return result

# def solve(solution, cards, costs):
#         
#     stack = [(solution)]
#         
#     result = -1
#     while stack:
#         solution = stack.pop()
#         # base case
#         if set_gcd(solution[1]) == 1 : 
#             if result == -1 : result = solution[0]
#             elif solution[0] < result : result = solution[0]
#             continue
#         # look for the result
#         for cost, card in zip(costs, cards):
#             if card not in solution[1] :
#                 stack.append((solution[0] + cost, solution[1].union([card])))
#         
#     return result

def solve(solution, cards, costs):
    
#     checked = []
    heap = [(solution)]
    while heap:
        solution = heap[0]
        heappop(heap)
        # base case
        if set_gcd(solution[1]) == 1 : return solution[0]
        # look for the result
        for cost, card in zip(costs, cards):
            if card not in solution[1] :
                s = solution[1].union([card])
#                 if s not in checked :
#                 checked.append(s)
                heappush(heap, (solution[0] + cost, s))
    return -1

if __name__ == '__main__':
    
    line = sys.stdin.readline()
    line = sys.stdin.readline().rstrip()
    cards = map(int, line.split())
    line = sys.stdin.readline().rstrip()
    costs = map(int, line.split())
    if len(set(cards)) != len(cards) : print('len differs')
    print(solve((0, set()), cards, costs))
      
#     cards = [100, 99, 9900]
#     costs = [1, 1, 1]
#     print(solve((0, set()), cards, costs)) # 2
#      
#     cards = [10, 20, 30, 40, 50]
#     costs = [1, 1, 1, 1, 1]
#     print(solve((0, set()), cards, costs)) # -1
#          
#     cards = [15015, 10010, 6006, 4290, 2730, 2310, 1]
#     costs = [1, 1, 1, 1, 1, 1, 10]
#     print(solve((0, set()), cards, costs)) # 6
#          
#     cards = [4264, 4921, 6321, 6984, 2316, 8432, 6120, 1026]
#     costs = [4264, 4921, 6321, 6984, 2316, 8432, 6120, 1026]
#     print(solve((0, set()), cards, costs)) # 7237