# Question: 4610
## Generation 1
### Conversations

---

**role**: 
````markdown
system
````

---

**content**: 
````markdown
I want you to act as a Coding Contest Participant. Imagine that you are taking part in a prestigious coding competition. Your task is to design an efficient algorithm for a complex problem. You need to consider all possible edge cases, optimize for efficiency, and ensure that your solution is clean and readable. In addition, provide a Python code of your solution, and put the solution in a code delimiter.For example:
### QUESTION
A. Watermelon
time limit per test: 1 second
memory limit per test: 64 megabytes
input: standard input
output: standard output
One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.

Input
The first (and the only) input line contains integer number w (1 <= w <= 100) — the weight of the watermelon bought by the boys.

Output
Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.

Examples
input
8
output
YES
Note
For example, the boys can divide the watermelon into two parts of 2 and 6 kilos respectively (another variant — two parts of 4 and 4 kilos).

### Expected response from you
#@!CODE START!@#
w = int(input())
if w % 2 == 1 or w < 4:
print("NO")
else:
print("YES")
#@!CODE END!@#
````

---

**role**: 
````markdown
user
````

---

**content**: 
````markdown
### QUESTION
Takahashi has N balls. Initially, an integer A_i is written on the i-th ball.
He would like to rewrite the integer on some balls so that there are at most K different integers written on the N balls.
Find the minimum number of balls that Takahashi needs to rewrite the integers on them.

-----Constraints-----
 - 1 \leq K \leq N \leq 200000
 - 1 \leq A_i \leq N
 - All input values are integers.

-----Input-----
Input is given from Standard Input in the following format:
N K
A_1 A_2 ... A_N

-----Output-----
Print the minimum number of balls that Takahashi needs to rewrite the integers on them.

-----Sample Input-----
5 2
1 1 2 2 5

-----Sample Output-----
1

For example, if we rewrite the integer on the fifth ball to 2, there are two different integers written on the balls: 1 and 2.
On the other hand, it is not possible to rewrite the integers on zero balls so that there are at most two different integers written on the balls, so we should print 1.
### Requirements
1. Use Standard Input Format (read inputs with `input()`, write results with `print()`)
2. You will NOT return anything except for the program. 
3. DO NOT WRITE PLANS OR EXPLANATIONS
````

---

**role**: 
````markdown
assistant
````

---

**content**: 
````markdown
#@!CODE START!@#
def minimum_rewrite(N, K, balls):
    freq = {}
    for ball in balls:
        if ball in freq:
            freq[ball] += 1
        else:
            freq[ball] = 1

    sorted_freq = sorted(freq.items(), key=lambda x: x[1])

    count = 0
    i = 0
    while len(sorted_freq) > K:
        count += sorted_freq[i][1]
        sorted_freq.pop(i)
        i += 1

    return count

# Read input
N, K = map(int, input().split())
balls = list(map(int, input().split()))

# Call the function and print the result
result = minimum_rewrite(N, K, balls)
print(result)
#@!CODE END!@#
````

---

