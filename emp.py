#given a list of strings, print \subsection{Example {index}: Unique id: {string}}\n

def print_latex_subsections(strings):
    for index, string in enumerate(strings):
        print(f"\\subsection{{Example {index+2}: Unique id: {string}}}\n") 

lista= [
"333\_gpt-4o",
"271\_gpt-4o",
"197\_llama3point1-70b",
"356\_gpt-4o"

]

print_latex_subsections(lista)