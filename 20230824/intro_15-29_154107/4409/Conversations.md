# Question: 4409
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
You are given an array $a$ consisting of $n$ integers. You can perform the following operations arbitrary number of times (possibly, zero):

  Choose a pair of indices $(i, j)$ such that $|i-j|=1$ (indices $i$ and $j$ are adjacent) and set $a_i := a_i + |a_i - a_j|$;  Choose a pair of indices $(i, j)$ such that $|i-j|=1$ (indices $i$ and $j$ are adjacent) and set $a_i := a_i - |a_i - a_j|$. 

The value $|x|$ means the absolute value of $x$. For example, $|4| = 4$, $|-3| = 3$.

Your task is to find the minimum number of operations required to obtain the array of equal elements and print the order of operations to do it.

It is guaranteed that you always can obtain the array of equal elements using such operations.

Note that after each operation each element of the current array should not exceed $10^{18}$ by absolute value.


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 2 \cdot 10^5$) — the number of elements in $a$.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($0 \le a_i \le 2 \cdot 10^5$), where $a_i$ is the $i$-th element of $a$.


-----Output-----

In the first line print one integer $k$ — the minimum number of operations required to obtain the array of equal elements.

In the next $k$ lines print operations itself. The $p$-th operation should be printed as a triple of integers $(t_p, i_p, j_p)$, where $t_p$ is either $1$ or $2$ ($1$ means that you perform the operation of the first type, and $2$ means that you perform the operation of the second type), and $i_p$ and $j_p$ are indices of adjacent elements of the array such that $1 \le i_p, j_p \le n$, $|i_p - j_p| = 1$. See the examples for better understanding.

Note that after each operation each element of the current array should not exceed $10^{18}$ by absolute value.

If there are many possible answers, you can print any.


-----Examples-----
Input
5
2 4 6 6 6

Output
2
1 2 3 
1 1 2 

Input
3
2 8 10

Output
2
2 2 1 
2 3 2 

Input
4
1 1 1 1

Output
0
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
def minimum_operations(n, a):
    operations = []
    count = 0
    for i in range(n-1):
        if a[i] != a[i+1]:
            count += 1
            if a[i] < a[i+1]:
                a[i] = a[i] + abs(a[i] - a[i+1])
                operations.append((1, i+1, i+2))
            else:
                a[i] = a[i] - abs(a[i] - a[i+1])
                operations.append((2, i+1, i+2))
    return count, operations

n = int(input())
a = list(map(int, input().split()))

count, operations = minimum_operations(n, a)

print(count)
for operation in operations:
    print(*operation)
#@!CODE END!@#
````

---

## Feedback 1
### Conversations

---

**role**: 
````markdown
system
````

---

**content**: 
````markdown
I want you to act as a Code Reviewer who will give feedback on a buggy program. Imagine that you've been given a piece of code that is causing unexpected results. Your task is to scrutinize the code, identify the bugs, and provide constructive feedback. Discuss your findings in detail: what are the bugs? Where in the code do they occur? What impact do they have on the program's functionality?

### Requirement
You will NOT SUGGEST SOLUTION, because the user wants to fix the bugs themselves.
You will NOT SUGGEST SOLUTION, because the user wants to fix the bugs themselves.
You will NOT SUGGEST SOLUTION, because the user wants to fix the bugs themselves.
You will NOT generate FINAL CODE, because the user wants to fix the bugs themselves.
You will NOT generate FINAL CODE, because the user wants to fix the bugs themselves.
You will NOT generate FINAL CODE, because the user wants to fix the bugs themselves.
You will NOT FIX the CODE, because the user wants to fix the bugs themselves.
You will NOT FIX the CODE, because the user wants to fix the bugs themselves.
You will NOT FIX the CODE, because the user wants to fix the bugs themselves.
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
You are given an array $a$ consisting of $n$ integers. You can perform the following operations arbitrary number of times (possibly, zero):

  Choose a pair of indices $(i, j)$ such that $|i-j|=1$ (indices $i$ and $j$ are adjacent) and set $a_i := a_i + |a_i - a_j|$;  Choose a pair of indices $(i, j)$ such that $|i-j|=1$ (indices $i$ and $j$ are adjacent) and set $a_i := a_i - |a_i - a_j|$. 

The value $|x|$ means the absolute value of $x$. For example, $|4| = 4$, $|-3| = 3$.

Your task is to find the minimum number of operations required to obtain the array of equal elements and print the order of operations to do it.

It is guaranteed that you always can obtain the array of equal elements using such operations.

Note that after each operation each element of the current array should not exceed $10^{18}$ by absolute value.


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 2 \cdot 10^5$) — the number of elements in $a$.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($0 \le a_i \le 2 \cdot 10^5$), where $a_i$ is the $i$-th element of $a$.


-----Output-----

In the first line print one integer $k$ — the minimum number of operations required to obtain the array of equal elements.

In the next $k$ lines print operations itself. The $p$-th operation should be printed as a triple of integers $(t_p, i_p, j_p)$, where $t_p$ is either $1$ or $2$ ($1$ means that you perform the operation of the first type, and $2$ means that you perform the operation of the second type), and $i_p$ and $j_p$ are indices of adjacent elements of the array such that $1 \le i_p, j_p \le n$, $|i_p - j_p| = 1$. See the examples for better understanding.

Note that after each operation each element of the current array should not exceed $10^{18}$ by absolute value.

If there are many possible answers, you can print any.


-----Examples-----
Input
5
2 4 6 6 6

Output
2
1 2 3 
1 1 2 

Input
3
2 8 10

Output
2
2 2 1 
2 3 2 

Input
4
1 1 1 1

Output
0
### INCORRECT PYTHON CODE
def minimum_operations(n, a):
    operations = []
    count = 0
    for i in range(n-1):
        if a[i] != a[i+1]:
            count += 1
            if a[i] < a[i+1]:
                a[i] = a[i] + abs(a[i] - a[i+1])
                operations.append((1, i+1, i+2))
            else:
                a[i] = a[i] - abs(a[i] - a[i+1])
                operations.append((2, i+1, i+2))
    return count, operations

n = int(input())
a = list(map(int, input().split()))

count, operations = minimum_operations(n, a)

print(count)
for operation in operations:
    print(*operation)
The code above is wrong and contains bugs. Given input "5
2 4 6 6 6
" the output was "2
1 1 2
1 2 3
" but the expected output was "2
1 2 3 
1 1 2 
".
````

---

## Repair 1
### Conversations

---

**role**: 
````markdown
system
````

---

**content**: 
````markdown
I want you to act as a Programmer who fixes bugs in programs based on feedback given. Picture yourself receiving a detailed review of a piece of code you've written, which contains several bugs. The feedback points out exactly where the errors lie and suggests improvements. Your task is to carefully analyze the feedback, understand the identified issues and the proposed solutions. Then, you need to implement these fixes in the code. Finally, provide a Python code of your implementation.
## Expected Response from you
#@!CODE START!@#
w = int(input())
if w % 2 == 1 or w == 2:
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
You are given an array $a$ consisting of $n$ integers. You can perform the following operations arbitrary number of times (possibly, zero):

  Choose a pair of indices $(i, j)$ such that $|i-j|=1$ (indices $i$ and $j$ are adjacent) and set $a_i := a_i + |a_i - a_j|$;  Choose a pair of indices $(i, j)$ such that $|i-j|=1$ (indices $i$ and $j$ are adjacent) and set $a_i := a_i - |a_i - a_j|$. 

The value $|x|$ means the absolute value of $x$. For example, $|4| = 4$, $|-3| = 3$.

Your task is to find the minimum number of operations required to obtain the array of equal elements and print the order of operations to do it.

It is guaranteed that you always can obtain the array of equal elements using such operations.

Note that after each operation each element of the current array should not exceed $10^{18}$ by absolute value.


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 2 \cdot 10^5$) — the number of elements in $a$.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($0 \le a_i \le 2 \cdot 10^5$), where $a_i$ is the $i$-th element of $a$.


-----Output-----

In the first line print one integer $k$ — the minimum number of operations required to obtain the array of equal elements.

In the next $k$ lines print operations itself. The $p$-th operation should be printed as a triple of integers $(t_p, i_p, j_p)$, where $t_p$ is either $1$ or $2$ ($1$ means that you perform the operation of the first type, and $2$ means that you perform the operation of the second type), and $i_p$ and $j_p$ are indices of adjacent elements of the array such that $1 \le i_p, j_p \le n$, $|i_p - j_p| = 1$. See the examples for better understanding.

Note that after each operation each element of the current array should not exceed $10^{18}$ by absolute value.

If there are many possible answers, you can print any.


-----Examples-----
Input
5
2 4 6 6 6

Output
2
1 2 3 
1 1 2 

Input
3
2 8 10

Output
2
2 2 1 
2 3 2 

Input
4
1 1 1 1

Output
0
### Requirement
Use Standard Input Format (read inputs with `input()`, write results with `print()`)
### INCORRECT PYTHON CODE
#@!CODE START!@#
def minimum_operations(n, a):
    operations = []
    count = 0
    for i in range(n-1):
        if a[i] != a[i+1]:
            count += 1
            if a[i] < a[i+1]:
                a[i] = a[i] + abs(a[i] - a[i+1])
                operations.append((1, i+1, i+2))
            else:
                a[i] = a[i] - abs(a[i] - a[i+1])
                operations.append((2, i+1, i+2))
    return count, operations

n = int(input())
a = list(map(int, input().split()))

count, operations = minimum_operations(n, a)

print(count)
for operation in operations:
    print(*operation)
#@!CODE END!@#
The code above is wrong and contains bugs. Given input "5
2 4 6 6 6
" the output was "2
1 1 2
1 2 3
" but the expected output was "2
1 2 3 
1 1 2 
".
The following is a detailed explanation of the issues: 
            ### BUGS

#### Bug 1
In line 9, the condition `if a[i] != a[i+1]:` is checking if the current element is different from the next element in the array. However, the problem statement specifies that the goal is to obtain an array of equal elements. So this condition should be inverted to `if a[i] == a[i+1]:`.

#### Bug 2
In line 14, when performing the first type of operation (setting `a[i] := a[i] + |a[i] - a[i+1]|`), the index of the second element in the operation should be `i+1`, not `i+2`. So the code should be changed to `operations.append((1, i+1, i+1))`.

#### Bug 3
In line 17, when performing the second type of operation (setting `a[i] := a[i] - |a[i] - a[i+1]|`), the index of the second element in the operation should be `i+1`, not `i+2`. So the code should be changed to `operations.append((2, i+1, i+1))`.

#### Bug 4
In the last line, the code is printing the operations in the wrong order. The operations should be printed in reverse order, so the code should be changed to `for operation in operations[::-1]:`.

#### Bug 5
In line 7, the variable `count` is not being updated correctly. Currently, it's counting the number of operations where the elements are different. However, this is not necessarily equal to the minimum number of operations required to obtain an array of equal elements. To fix this, we need to change the condition in line 9 to `if a[i] == a[i+1]:` and also add a check after the loop to see if `count` is odd. If it is, increment it by 1.

#### Bug 6
In line 11, the code is incorrectly updating `a[i]` by adding or subtracting `|a[i] - a[i+1]|`. According to the problem statement, `a[i]` should be updated based on the absolute difference between `a[i+1]` and the original value of `a[i]` before any operations were performed. So the code should be changed to `a[i] = a[i+1] + abs(a[i] - a[i+1])` for the first type of operation and `a[i] = a[i+1] - abs(a[i] - a[i+1])` for the second type of operation.

#### Bug 7
In lines 11 and 15, the code is incorrectly updating `a[i]` using the absolute difference between `a[i]` and `a[i+1]`. According to the problem statement, the absolute difference should be added/subtracted to/from `a[i]`, not used as the new value of `a[i]`. So the code should be changed to `a[i] += abs(a[i] - a[i+1])` for the first type of operation and `a[i] -= abs(a[i] - a[i+1])` for the second type of operation.

### IMPACT

- Bug 1: This bug causes the code to only perform operations when adjacent elements are the same, instead of when adjacent elements are different. This can lead to incorrect results if there are adjacent elements that are different.

- Bug 2: This bug causes the code to add the incorrect index of the second element in the first type of operation. This will lead to incorrect operations being printed.

- Bug 3: This bug causes the code to add the incorrect index of the second element in the second type of operation. This will lead to incorrect operations being printed.

- Bug 4: This bug causes the code to print the operations in the wrong order. Instead of printing the operations in reverse order, the code is currently printing them in the order they were performed. This will lead to incorrect output.

- Bug 5: This bug causes the code to incorrectly calculate the minimum number of operations required. By counting the number of operations where the elements are different, the code is not considering cases where multiple operations can be combined into a single operation.

- Bug 6: This bug causes the code to incorrectly update `a[i]` by adding/subtracting the absolute difference between `a[i]` and `a[i+1]`. This will lead to incorrect values for `a[i]` after each operation.

- Bug 7: This bug causes the code to incorrectly update `a[i]` using the absolute difference between `a[i]` and `a[i+1]` as the new value of `a[i]`. This will lead to incorrect values for `a[i]` after each operation.
````

---

**role**: 
````markdown
assistant
````

---

**content**: 
````markdown
### BUGS FIXED PYTHON CODE
#@!CODE START!@#
def minimum_operations(n, a):
    operations = []
    count = 0
    for i in range(n-1):
        if a[i] == a[i+1]:
            count += 1
            if a[i] < a[i+1]:
                a[i] += abs(a[i] - a[i+1])
                operations.append((1, i+1, i+1))
            else:
                a[i] -= abs(a[i] - a[i+1])
                operations.append((2, i+1, i+1))
    
    if count % 2 == 1:
        count += 1
        
    return count, operations[::-1]

n = int(input())
a = list(map(int, input().split()))

count, operations = minimum_operations(n, a)

print(count)
for operation in operations:
    print(*operation)
#@!CODE END!@#
````

---

