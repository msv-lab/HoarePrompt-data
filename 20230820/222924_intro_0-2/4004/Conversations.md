# Question: 4004
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
You are given a sequence $a_1, a_2, \dots, a_n$ consisting of $n$ integers.

You can choose any non-negative integer $D$ (i.e. $D \ge 0$), and for each $a_i$ you can:

  add $D$ (only once), i. e. perform $a_i := a_i + D$, or  subtract $D$ (only once), i. e. perform $a_i := a_i - D$, or  leave the value of $a_i$ unchanged. 

It is possible that after an operation the value $a_i$ becomes negative.

Your goal is to choose such minimum non-negative integer $D$ and perform changes in such a way, that all $a_i$ are equal (i.e. $a_1=a_2=\dots=a_n$).

Print the required $D$ or, if it is impossible to choose such value $D$, print -1.

For example, for array $[2, 8]$ the value $D=3$ is minimum possible because you can obtain the array $[5, 5]$ if you will add $D$ to $2$ and subtract $D$ from $8$. And for array $[1, 4, 7, 7]$ the value $D=3$ is also minimum possible. You can add it to $1$ and subtract it from $7$ and obtain the array $[4, 4, 4, 4]$.


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 100$) — the number of elements in $a$.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 100$) — the sequence $a$.


-----Output-----

Print one integer — the minimum non-negative integer value $D$ such that if you add this value to some $a_i$, subtract this value from some $a_i$ and leave some $a_i$ without changes, all obtained values become equal.

If it is impossible to choose such value $D$, print -1.


-----Examples-----
Input
6
1 4 4 7 4 1

Output
3

Input
5
2 2 5 2 5

Output
3

Input
4
1 3 3 7

Output
-1

Input
2
2 8

Output
3
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
def find_minimum_D(n, a):
    min_a = min(a)
    max_a = max(a)
    if min_a == max_a:
        return 0
    elif (max_a - min_a) % (n-1) != 0:
        return -1
    else:
        D = (max_a - min_a) // (n-1)
        for i in range(n):
            if a[i] - min_a > D or (a[i] - min_a) % D != 0:
                return -1
        return D

n = int(input())
a = list(map(int, input().split()))

result = find_minimum_D(n, a)
print(result)
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
You are given a sequence $a_1, a_2, \dots, a_n$ consisting of $n$ integers.

You can choose any non-negative integer $D$ (i.e. $D \ge 0$), and for each $a_i$ you can:

  add $D$ (only once), i. e. perform $a_i := a_i + D$, or  subtract $D$ (only once), i. e. perform $a_i := a_i - D$, or  leave the value of $a_i$ unchanged. 

It is possible that after an operation the value $a_i$ becomes negative.

Your goal is to choose such minimum non-negative integer $D$ and perform changes in such a way, that all $a_i$ are equal (i.e. $a_1=a_2=\dots=a_n$).

Print the required $D$ or, if it is impossible to choose such value $D$, print -1.

For example, for array $[2, 8]$ the value $D=3$ is minimum possible because you can obtain the array $[5, 5]$ if you will add $D$ to $2$ and subtract $D$ from $8$. And for array $[1, 4, 7, 7]$ the value $D=3$ is also minimum possible. You can add it to $1$ and subtract it from $7$ and obtain the array $[4, 4, 4, 4]$.


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 100$) — the number of elements in $a$.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 100$) — the sequence $a$.


-----Output-----

Print one integer — the minimum non-negative integer value $D$ such that if you add this value to some $a_i$, subtract this value from some $a_i$ and leave some $a_i$ without changes, all obtained values become equal.

If it is impossible to choose such value $D$, print -1.


-----Examples-----
Input
6
1 4 4 7 4 1

Output
3

Input
5
2 2 5 2 5

Output
3

Input
4
1 3 3 7

Output
-1

Input
2
2 8

Output
3
### INCORRECT PYTHON CODE
def find_minimum_D(n, a):
    min_a = min(a)
    max_a = max(a)
    if min_a == max_a:
        return 0
    elif (max_a - min_a) % (n-1) != 0:
        return -1
    else:
        D = (max_a - min_a) // (n-1)
        for i in range(n):
            if a[i] - min_a > D or (a[i] - min_a) % D != 0:
                return -1
        return D

n = int(input())
a = list(map(int, input().split()))

result = find_minimum_D(n, a)
print(result)
The code above is wrong and contains bugs. Given input "6
1 4 4 7 4 1
" the output was "-1
" but the expected output was "3
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
You are given a sequence $a_1, a_2, \dots, a_n$ consisting of $n$ integers.

You can choose any non-negative integer $D$ (i.e. $D \ge 0$), and for each $a_i$ you can:

  add $D$ (only once), i. e. perform $a_i := a_i + D$, or  subtract $D$ (only once), i. e. perform $a_i := a_i - D$, or  leave the value of $a_i$ unchanged. 

It is possible that after an operation the value $a_i$ becomes negative.

Your goal is to choose such minimum non-negative integer $D$ and perform changes in such a way, that all $a_i$ are equal (i.e. $a_1=a_2=\dots=a_n$).

Print the required $D$ or, if it is impossible to choose such value $D$, print -1.

For example, for array $[2, 8]$ the value $D=3$ is minimum possible because you can obtain the array $[5, 5]$ if you will add $D$ to $2$ and subtract $D$ from $8$. And for array $[1, 4, 7, 7]$ the value $D=3$ is also minimum possible. You can add it to $1$ and subtract it from $7$ and obtain the array $[4, 4, 4, 4]$.


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 100$) — the number of elements in $a$.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 100$) — the sequence $a$.


-----Output-----

Print one integer — the minimum non-negative integer value $D$ such that if you add this value to some $a_i$, subtract this value from some $a_i$ and leave some $a_i$ without changes, all obtained values become equal.

If it is impossible to choose such value $D$, print -1.


-----Examples-----
Input
6
1 4 4 7 4 1

Output
3

Input
5
2 2 5 2 5

Output
3

Input
4
1 3 3 7

Output
-1

Input
2
2 8

Output
3
### Requirement
Use Standard Input Format (read inputs with `input()`, write results with `print()`)
### INCORRECT PYTHON CODE
#@!CODE START!@#
def find_minimum_D(n, a):
    min_a = min(a)
    max_a = max(a)
    if min_a == max_a:
        return 0
    elif (max_a - min_a) % (n-1) != 0:
        return -1
    else:
        D = (max_a - min_a) // (n-1)
        for i in range(n):
            if a[i] - min_a > D or (a[i] - min_a) % D != 0:
                return -1
        return D

n = int(input())
a = list(map(int, input().split()))

result = find_minimum_D(n, a)
print(result)
#@!CODE END!@#
The code above is wrong and contains bugs. Given input "6
1 4 4 7 4 1
" the output was "-1
" but the expected output was "3
".
The following is a detailed explanation of the issues: 
            ### ANALYSIS
There are several bugs in the given code:

1. The condition `if min_a == max_a` returns `0` when `min_a` and `max_a` are equal. However, this condition should return `0` only if all the elements in the array `a` are equal. In the provided test case, the array is `[1, 4, 4, 7, 4, 1]`, where `min_a = 1` and `max_a = 7`. Since not all elements are equal, this condition should return `-1`.

2. The condition `(max_a - min_a) % (n-1) != 0` checks if the difference between the maximum and minimum elements in the array is divisible by `(n-1)`. This condition is incorrect because it assumes that the minimum and maximum elements should be equal after making the required changes. However, this is not always the case. In the provided test case, the array is `[1, 4, 4, 7, 4, 1]`, where `min_a = 1` and `max_a = 7`. The difference `max_a - min_a = 6` is not divisible by `(n-1) = 5`, but it is still possible to choose a value of `D` such that all elements become equal.

3. The loop `for i in range(n)` checks if each element in the array can be equalized by the chosen value of `D`. However, this loop only checks if the difference between each element and the minimum element is divisible by `D`. This is incorrect because it assumes that the minimum element should be equalized with the other elements. In the provided test case, the array is `[1, 4, 4, 7, 4, 1]` and the minimum element is `1`. The loop checks if each element can be equalized with `1`, which is incorrect. It should instead check if each element can be equalized with a certain value of `D` (which is not necessarily equal to the minimum element).

4. The code does not handle the case where it is impossible to choose such a value of `D` to equalize all elements. The given code returns `-1` in some cases, but it does not consider all possible scenarios where it is impossible to get all elements to be equal.

### BUGS SUMMARY
1. The condition `if min_a == max_a` is incorrect.
2. The condition `(max_a - min_a) % (n-1) != 0` is incorrect.
3. The loop `for i in range(n)` checks incorrect condition for equalizing elements.
4. The code does not handle the case where equalizing all elements is impossible.

### SUGGESTED IMPROVEMENTS
Here are the suggested improvements to the code:

1. Check if all elements in the array are equal and return `-1` if they are not.

2. Find the minimum and maximum elements in the array.

3. Iterate over all possible values of `D` from `0` to `max_a - min_a` and check if it is possible to equalize all elements using that value of `D`. To check this, iterate over each element in the array and find the number of changes required to make it equal to other elements. If the number of changes is not divisible by `2`, then it is not possible to equalize all elements and continue to the next value of `D`. If all elements can be equalized using a certain value of `D`, return that value of `D`. If it is not possible to equalize all elements for any value of `D`, return `-1`.
````

---

**role**: 
````markdown
assistant
````

---

**content**: 
````markdown
### CORRECTED PYTHON CODE
#@!CODE START!@#
def find_minimum_D(n, a):
    min_a = min(a)
    max_a = max(a)
    
    if min_a != max_a:
        for D in range(max_a - min_a + 1):
            changes = 0
            for i in range(n):
                changes += (abs(a[i] - (min_a + D)) % D)
            if changes % 2 == 0:
                return D
                
    return -1


n = int(input())
a = list(map(int, input().split()))

result = find_minimum_D(n, a)

print(result)
#@!CODE END!@#
````

---

## Generation 2
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
You are given a sequence $a_1, a_2, \dots, a_n$ consisting of $n$ integers.

You can choose any non-negative integer $D$ (i.e. $D \ge 0$), and for each $a_i$ you can:

  add $D$ (only once), i. e. perform $a_i := a_i + D$, or  subtract $D$ (only once), i. e. perform $a_i := a_i - D$, or  leave the value of $a_i$ unchanged. 

It is possible that after an operation the value $a_i$ becomes negative.

Your goal is to choose such minimum non-negative integer $D$ and perform changes in such a way, that all $a_i$ are equal (i.e. $a_1=a_2=\dots=a_n$).

Print the required $D$ or, if it is impossible to choose such value $D$, print -1.

For example, for array $[2, 8]$ the value $D=3$ is minimum possible because you can obtain the array $[5, 5]$ if you will add $D$ to $2$ and subtract $D$ from $8$. And for array $[1, 4, 7, 7]$ the value $D=3$ is also minimum possible. You can add it to $1$ and subtract it from $7$ and obtain the array $[4, 4, 4, 4]$.


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 100$) — the number of elements in $a$.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 100$) — the sequence $a$.


-----Output-----

Print one integer — the minimum non-negative integer value $D$ such that if you add this value to some $a_i$, subtract this value from some $a_i$ and leave some $a_i$ without changes, all obtained values become equal.

If it is impossible to choose such value $D$, print -1.


-----Examples-----
Input
6
1 4 4 7 4 1

Output
3

Input
5
2 2 5 2 5

Output
3

Input
4
1 3 3 7

Output
-1

Input
2
2 8

Output
3
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
n = int(input())
a = list(map(int, input().split()))

# Find the minimum and maximum values in the array
min_a = min(a)
max_a = max(a)

# If all elements are already equal, we don't need to make any changes
if min_a == max_a:
    print(0)
else:
    # Check if it is possible to make all elements equal by adding or subtracting a certain amount
    possible_values = set([(max_a - min_a) // (n-1) * i + min_a for i in range(n)])
    
    # Check if any of the possible values make all elements equal
    for value in possible_values:
        if all((ai - value) % (value - min_a) == 0 or (ai - min_a) % (value - min_a) == 0 for ai in a):
            print(value - min_a)
            exit()
    
    # If no such value exists, it is impossible to make all elements equal
    print(-1)
    
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
You are given a sequence $a_1, a_2, \dots, a_n$ consisting of $n$ integers.

You can choose any non-negative integer $D$ (i.e. $D \ge 0$), and for each $a_i$ you can:

  add $D$ (only once), i. e. perform $a_i := a_i + D$, or  subtract $D$ (only once), i. e. perform $a_i := a_i - D$, or  leave the value of $a_i$ unchanged. 

It is possible that after an operation the value $a_i$ becomes negative.

Your goal is to choose such minimum non-negative integer $D$ and perform changes in such a way, that all $a_i$ are equal (i.e. $a_1=a_2=\dots=a_n$).

Print the required $D$ or, if it is impossible to choose such value $D$, print -1.

For example, for array $[2, 8]$ the value $D=3$ is minimum possible because you can obtain the array $[5, 5]$ if you will add $D$ to $2$ and subtract $D$ from $8$. And for array $[1, 4, 7, 7]$ the value $D=3$ is also minimum possible. You can add it to $1$ and subtract it from $7$ and obtain the array $[4, 4, 4, 4]$.


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 100$) — the number of elements in $a$.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 100$) — the sequence $a$.


-----Output-----

Print one integer — the minimum non-negative integer value $D$ such that if you add this value to some $a_i$, subtract this value from some $a_i$ and leave some $a_i$ without changes, all obtained values become equal.

If it is impossible to choose such value $D$, print -1.


-----Examples-----
Input
6
1 4 4 7 4 1

Output
3

Input
5
2 2 5 2 5

Output
3

Input
4
1 3 3 7

Output
-1

Input
2
2 8

Output
3
### INCORRECT PYTHON CODE
n = int(input())
a = list(map(int, input().split()))

# Find the minimum and maximum values in the array
min_a = min(a)
max_a = max(a)

# If all elements are already equal, we don't need to make any changes
if min_a == max_a:
    print(0)
else:
    # Check if it is possible to make all elements equal by adding or subtracting a certain amount
    possible_values = set([(max_a - min_a) // (n-1) * i + min_a for i in range(n)])
    
    # Check if any of the possible values make all elements equal
    for value in possible_values:
        if all((ai - value) % (value - min_a) == 0 or (ai - min_a) % (value - min_a) == 0 for ai in a):
            print(value - min_a)
            exit()
    
    # If no such value exists, it is impossible to make all elements equal
    print(-1)
    
The code above is wrong and contains bugs. Given input "6
1 4 4 7 4 1
" the output was "Traceback (most recent call last):
  File "/var/folders/46/8ybh48tn40l32kbzy6n99p380000gn/T/tmpin5nskvm.py", line 17, in <module>
    if all((ai - value) % (value - min_a) == 0 or (ai - min_a) % (value - min_a) == 0 for ai in a):
  File "/var/folders/46/8ybh48tn40l32kbzy6n99p380000gn/T/tmpin5nskvm.py", line 17, in <genexpr>
    if all((ai - value) % (value - min_a) == 0 or (ai - min_a) % (value - min_a) == 0 for ai in a):
ZeroDivisionError: integer division or modulo by zero
" but the expected output was "3
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
You are given a sequence $a_1, a_2, \dots, a_n$ consisting of $n$ integers.

You can choose any non-negative integer $D$ (i.e. $D \ge 0$), and for each $a_i$ you can:

  add $D$ (only once), i. e. perform $a_i := a_i + D$, or  subtract $D$ (only once), i. e. perform $a_i := a_i - D$, or  leave the value of $a_i$ unchanged. 

It is possible that after an operation the value $a_i$ becomes negative.

Your goal is to choose such minimum non-negative integer $D$ and perform changes in such a way, that all $a_i$ are equal (i.e. $a_1=a_2=\dots=a_n$).

Print the required $D$ or, if it is impossible to choose such value $D$, print -1.

For example, for array $[2, 8]$ the value $D=3$ is minimum possible because you can obtain the array $[5, 5]$ if you will add $D$ to $2$ and subtract $D$ from $8$. And for array $[1, 4, 7, 7]$ the value $D=3$ is also minimum possible. You can add it to $1$ and subtract it from $7$ and obtain the array $[4, 4, 4, 4]$.


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 100$) — the number of elements in $a$.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 100$) — the sequence $a$.


-----Output-----

Print one integer — the minimum non-negative integer value $D$ such that if you add this value to some $a_i$, subtract this value from some $a_i$ and leave some $a_i$ without changes, all obtained values become equal.

If it is impossible to choose such value $D$, print -1.


-----Examples-----
Input
6
1 4 4 7 4 1

Output
3

Input
5
2 2 5 2 5

Output
3

Input
4
1 3 3 7

Output
-1

Input
2
2 8

Output
3
### Requirement
Use Standard Input Format (read inputs with `input()`, write results with `print()`)
### INCORRECT PYTHON CODE
#@!CODE START!@#
n = int(input())
a = list(map(int, input().split()))

# Find the minimum and maximum values in the array
min_a = min(a)
max_a = max(a)

# If all elements are already equal, we don't need to make any changes
if min_a == max_a:
    print(0)
else:
    # Check if it is possible to make all elements equal by adding or subtracting a certain amount
    possible_values = set([(max_a - min_a) // (n-1) * i + min_a for i in range(n)])
    
    # Check if any of the possible values make all elements equal
    for value in possible_values:
        if all((ai - value) % (value - min_a) == 0 or (ai - min_a) % (value - min_a) == 0 for ai in a):
            print(value - min_a)
            exit()
    
    # If no such value exists, it is impossible to make all elements equal
    print(-1)
    
#@!CODE END!@#
The code above is wrong and contains bugs. Given input "6
1 4 4 7 4 1
" the output was "Traceback (most recent call last):
  File "/var/folders/46/8ybh48tn40l32kbzy6n99p380000gn/T/tmpin5nskvm.py", line 17, in <module>
    if all((ai - value) % (value - min_a) == 0 or (ai - min_a) % (value - min_a) == 0 for ai in a):
  File "/var/folders/46/8ybh48tn40l32kbzy6n99p380000gn/T/tmpin5nskvm.py", line 17, in <genexpr>
    if all((ai - value) % (value - min_a) == 0 or (ai - min_a) % (value - min_a) == 0 for ai in a):
ZeroDivisionError: integer division or modulo by zero
" but the expected output was "3
".
The following is a detailed explanation of the issues: 
            ### ANALYSIS

The given code is attempting to find the minimum non-negative integer value $D$ such that all elements in the array $a$ become equal. Let's analyze the bugs in the code:

1) **ZeroDivisionError**: This error occurs when the variable `value` is equal to `min_a`. In such cases, the expression `(value - min_a)` will be zero, leading to a division by zero error. This happens because the code assumes that the minimum value in the array will not be equal to the maximum value.

2) **Incorrect calculation of possible values**: The code attempts to find possible values of `value` by iterating over a range of `n` and performing calculations using the minimum and maximum values in the array. However, the calculation `(max_a - min_a) // (n-1) * i + min_a` is incorrect. It should be `(max_a - min_a) // (n-1) * i + min_a + 1` to ensure that all possible values of `value` are considered.

3) **Incorrect check for equal elements**: The code attempts to check if all elements become equal after adding or subtracting the calculated `value`. However, the expressions `(ai - value) % (value - min_a) == 0 or (ai - min_a) % (value - min_a) == 0` are incorrect. It should be `(ai - value) % (value - min_a) == 0 or (ai - min_a) % (value - min_a) == 0 or ai == value`.

### BUGGY CODE
````

---

**role**: 
````markdown
assistant
````

---

**content**: 
````markdown
n = int(input())
a = list(map(int, input().split()))

# Find the minimum and maximum values in the array
min_a = min(a)
max_a = max(a)

# If all elements are already equal, we don't need to make any changes
if min_a == max_a:
    print(0)
else:
    # Check if it is possible to make all elements equal by adding or subtracting a certain amount
    possible_values = set([(max_a - min_a) // (n-1) * i + min_a for i in range(n)])
    
    # Check if any of the possible values make all elements equal
    for value in possible_values:
        if all((ai - value) % (value - min_a) == 0 or (ai - min_a) % (value - min_a) == 0 or ai == value for ai in a):
            print(value - min_a)
            exit()
    
    # If no such value exists, it is impossible to make all elements equal
    print(-1)
````

---

**role**: 
````markdown
user
````

---

**content**: 
````markdown
continue
````

---

**role**: 
````markdown
assistant
````

---

**content**: 
````markdown
### CORRECT PYTHON CODE
#@!CODE START!@#
n = int(input())
a = list(map(int, input().split()))

# Find the minimum and maximum values in the array
min_a = min(a)
max_a = max(a)

# If all elements are already equal, we don't need to make any changes
if min_a == max_a:
    print(0)
else:
    # Check if it is possible to make all elements equal by adding or subtracting a certain amount
    if (max_a - min_a) % (n-1) == 0:
        value = (max_a - min_a) // (n-1)
        
        # Check if all elements become equal after adding or subtracting the calculated value
        if all((ai - value) % value == 0 or ai == min_a for ai in a):
            print(value)
            exit()
    
    # If no such value exists, it is impossible to make all elements equal
    print(-1)
#@!CODE END!@#
````

---

