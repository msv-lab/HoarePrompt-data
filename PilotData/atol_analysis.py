import json
from pathlib import Path
from datetime import datetime
from model import get_model

ATOL_ANALYSIS_PROMPT = """
You are an expert in numerical computing and programming. Your task is to analyze a programming problem and determine the appropriate absolute tolerance (atol) for comparing outputs.

Here is the problem description:

{prompt}

Please analyze whether this problem requires exact matching (atol=0) or needs some tolerance for floating point comparisons. 
If the problem:
- Involves only integers or exact string matching, use atol=0
- Involves floating point calculations (like math.pi, sqrt, trigonometric functions), suggest a small tolerance like atol=0.0001
- Involves complex numerical computations that could accumulate error, suggest a larger tolerance like atol=0.001 or atol=0.01

Return just the number (e.g. 0 or 0.0001 or 0.001):
"""

def analyze_atol(data_file: Path, output_file: Path):
    # Create output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Load the input data
    with open(data_file, 'r') as f:
        data = []
        for line in f:
            data.append(json.loads(line))
    
    # Initialize the model
    model = get_model("gpt-4o-2024-05-13", temperature=0)
    
    # Process each problem
    for item in data:
        if 'prompt' not in item:
            continue
            
        # Format the prompt with the question
        prompt = ATOL_ANALYSIS_PROMPT.format(prompt=item['prompt'])
        
        # Query the model
        response = model.query(prompt)
        
        # Parse the response and convert to float
        try:
            new_atol = float(response.strip())
            item['atol'] = new_atol
            print(f"Processed task {item.get('task_id', 'unknown')}: atol = {new_atol}")
        except ValueError:
            print(f"Warning: Could not parse atol value for task {item.get('task_id', 'unknown')}")
            continue
    
    # Save the results
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
    
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    # Input file
    input_file = Path("MbppPlus2.jsonl")
    
    # Output file with timestamp
    timestamp = datetime.now().strftime("%Y%m%d")
    output_file = Path(f"mbpp_with_atol_{timestamp}.jsonl")
    
    analyze_atol(input_file, output_file) 