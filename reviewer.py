import subprocess
import sys

def parse_flake8_output(output):
    """
    Converts raw flake8 output string into a clean list of formatted errors.
    """
    print("--- Parsing Output ---")
    formatted_errors = []
    
    # Split the raw output block into individual lines
    lines = output.strip().split('\n')
    
    for line in lines:
        # Sometimes flake8 adds empty lines, let's skip them
        if not line:
            continue
            
        # Split the line into its core parts
        # Example: 'test_docstrings.py:1:1: D100 Missing docstring...'
        parts = line.split(':', 3) # Split on the first 3 colons
        
        if len(parts) == 4:
            # We have filename, line_num, char_num, error_message
            filename = parts[0]
            line_num = parts[1]
            char_num = parts[2]
            error_message = parts[3].strip() # .strip() cleans up whitespace
            
            # Format it nicely
            error_string = f"⚠️ Error at Line {line_num}: {error_message}"
            formatted_errors.append(error_string)
            
    print("--- Parsing Complete ---")
    return formatted_errors

def analyze_code(filename):
    """
    Runs flake8 on a given file and returns a list of formatted errors.
    """
    print(f"--- Analyzing {filename} ---")
    
    command = [sys.executable, "-m", "flake8", filename]
    
    # We add a --config flag to tell flake8 to ignore the .flake8 file
    # This ensures we get the docstring errors for this test.
    command.append("--ignore=E501") # Let's also ignore "line too long"
    
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    print("--- Analysis Complete ---")
    
    # Now, we pass the raw output to our new parser
    return parse_flake8_output(result.stdout)

# --- Main part of the script ---
if __name__ == "__main__":
    file_to_test = "test_docstrings.py" 
    errors = analyze_code(file_to_test)
    
    # Print the final, clean list
    print("\n=== Formatted Report ===")
    if errors:
        for error in errors:
            print(error)
    else:
        print("✅ No errors found!")