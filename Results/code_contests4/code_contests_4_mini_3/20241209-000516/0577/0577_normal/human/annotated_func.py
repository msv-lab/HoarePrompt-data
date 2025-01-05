#State of the program right berfore the function call: x is an integer representing the person number in the family tree (1 ≤ x ≤ n), and dep is a positive integer representing the depth level in the family tree (1 ≤ dep ≤ n).
def func_1(x, dep):
    while x != -1:
        if nowChild[x] == lenChild[x]:
            if x != 0:
                ans[x][dep] = {ss[x]}
                for nowlistindex in range(0, len(query[x]), 2):
                    i = query[x][nowlistindex]
                    j = query[x][nowlistindex + 1]
                    if dep + i not in ans[x]:
                        answer[j] = 0
                    else:
                        answer[j] = len(ans[x][dep + i])
                """count ans"""
                if len(ans[x]) < len(ans[fa[x]]):
                    for j in ans[x]:
                        if j not in ans[fa[x]]:
                            ans[fa[x]][j] = ans[x][j]
                        elif len(ans[x][j]) < len(ans[fa[x]][j]):
                            ans[fa[x]][j] |= ans[x][j]
                            ans[x][j].clear()
                        else:
                            ans[x][j] |= ans[fa[x]][j]
                            ans[fa[x]][j].clear()
                            ans[fa[x]][j] = ans[x][j]
                    ans[x].clear()
                else:
                    for j in ans[fa[x]]:
                        if j not in ans[x]:
                            ans[x][j] = ans[fa[x]][j]
                        elif len(ans[x][j]) > len(ans[fa[x]][j]):
                            ans[x][j] |= ans[fa[x]][j]
                            ans[fa[x]][j].clear()
                        else:
                            ans[fa[x]][j] |= ans[x][j]
                            ans[x][j].clear()
                            ans[x][j] = ans[fa[x]][j]
                    ans[fa[x]].clear()
                    ans[fa[x]] = ans[x]
            x = fa[x]
            nowChild[x] += 1
            dep -= 1
        else:
            x = Child[x][nowChild[x]]
            dep += 1
        
    #State of the program after the loop has been executed: `x` is -1, `dep` is decremented to a value less than the initial depth, `nowChild` has been incremented for all ancestors of the original `x`, and `ans` has been updated based on the relationships defined in `query` and the family structure.
#Overall this is what the function does:The function accepts an integer `x` (representing a person in a family tree) and a positive integer `dep` (representing a depth level). It traverses the family tree to update the `ans` data structure based on the relationships defined in `query`, modifying `ans` for each ancestor of `x` and adjusting `nowChild` and `dep` accordingly. The function does not return any value explicitly, and its primary purpose is to update the global state of `ans`, reflecting the relationships and queries related to the specified person at the given depth.

