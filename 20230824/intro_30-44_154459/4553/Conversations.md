# Question: 4553
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
The postal code in Atcoder Kingdom is A+B+1 characters long, its (A+1)-th character is a hyphen -, and the other characters are digits from 0 through 9.
You are given a string S. Determine whether it follows the postal code format in Atcoder Kingdom.

-----Constraints-----
 - 1≤A,B≤5
 - |S|=A+B+1
 - S consists of - and digits from 0 through 9.

-----Input-----
Input is given from Standard Input in the following format:
A B
S

-----Output-----
Print Yes if S follows the postal code format in AtCoder Kingdom; print No otherwise.

-----Sample Input-----
3 4
269-6650

-----Sample Output-----
Yes

The (A+1)-th character of S is -, and the other characters are digits from 0 through 9, so it follows the format.
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
def check_postal_code_format(A, B, S):
    if len(S) != A + B + 1:
        return "No"
    if S[A] != "-":
        return "No"
    for i in range(len(S)):
        if i != A and not S[i].isdigit():
            return "No"
    return "Yes"

A, B = map(int, input().split())
S = input()
print(check_postal_code_format(A, B, S))
#@!CODE END!@#
````

---

