#State of the program right berfore the function call: expression is a string containing only parentheses ('(', ')'), square brackets ('[', ']'), and curly braces ('{', '}').
def func_1(expression):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    for char in expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
        
    #State of the program after the  for loop has been executed: Let's analyze the loop step by step and deduce the final state of the variables after all iterations of the loop have finished.
    #
    #### Initial State
    #- `stack` is an empty list.
    #- `brackets` is a dictionary containing `{'(': ')', '{': '}', '[': ']'}`.
    #- `expression` is a non-empty string.
    #
    #### Loop Code
    #```python
    #for char in expression:
    #    if char in brackets:
    #        stack.append(char)
    #    elif char in brackets.values():
    #        if not stack or brackets[stack.pop()] != char:
    #            return False
    #```
    #
    #### Analysis
    #
    #1. **First Iteration**:
    #   - If `char` is an opening bracket (`'('`, `'{'`, `'['`), it gets appended to `stack`.
    #   - If `char` is a closing bracket (`')'`, `'}'`, `']'`), it checks if `stack` is empty or if the last element of `stack` matches the corresponding opening bracket. If either condition fails, the function returns `False`.
    #
    #2. **Second Iteration**:
    #   - The process continues as described above. If an opening bracket is found, it gets appended to `stack`.
    #   - If a closing bracket is found, it checks if the top of `stack` matches the corresponding opening bracket. If it doesn't match, the function returns `False`.
    #
    #3. **Third Iteration**:
    #   - This pattern continues. If an opening bracket is found, it gets appended to `stack`.
    #   - If a closing bracket is found, it checks if the top of `stack` matches the corresponding opening bracket. If it doesn't match, the function returns `False`.
    #
    #4. **General Iteration**:
    #   - Each iteration appends an opening bracket to `stack` if found in `brackets`.
    #   - Each iteration pops the top element of `stack` and checks if it matches the current closing bracket. If they don't match, the function returns `False`.
    #
    #5. **Final State**:
    #   - After all iterations, if there are no mismatches and the `stack` is empty, the function returns `True`.
    #   - If there are mismatches or the `stack` is not empty, the function returns `False`.
    #
    #### Output State
    #
    #Given the above analysis, the final state of the variables after all iterations of the loop have finished can be summarized as follows:
    #
    #- `stack` will be empty if and only if the `expression` is a valid sequence of matching brackets. If the `expression` contains any mismatched brackets or unbalanced sequences, the `stack` will not be empty.
    #- `brackets` remains unchanged as it is a dictionary defined in the initial state.
    #- The function returns `True` if the `stack` is empty at the end, indicating all brackets are correctly matched. It returns `False` otherwise.
    #
    #**Output State:**
    #- `stack` is empty if and only if the `expression` is a valid sequence of matching brackets. Otherwise, `stack` contains unmatched opening brackets.
    #- `brackets` is {'(': ')', '{': '}', '[': ']'}.
    #- The function returns `True` if the `stack` is empty, and `False` otherwise.
    return not stack
    #The program returns True if the stack is empty (indicating all brackets are correctly matched) and False if the stack is not empty (indicating there are unmatched opening brackets). Brackets remain as {'(': ')', '{': '}', '[': ']'}
#Overall this is what the function does:The function `func_1` accepts a string `expression` containing only parentheses (`(`, `)`), square brackets (`[`, `]`), and curly braces (`{`, `}`) and returns a boolean value indicating whether all brackets in the string are correctly matched.

