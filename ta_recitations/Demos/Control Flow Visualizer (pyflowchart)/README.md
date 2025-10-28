#### Introduction
[pyflowchart](https://pypi.org/project/pyflowchart/) is a pretty neat module which can take your Python code (as a file) and generate a flowchart of the program execution!

This can (at times) be very helpful as you learn how control flow (if-elif-else, for, while) works for visual learners.

#### Tutorial
```bash
# Step 1: Install the Module
pip install pyflowchart

# Step 2: Using the terminal, cd into the directory that contains your python file
cd "Control Flow Visualizer (pyflowchart)"

# Step 3: Generate the HTML Diagram
python -m pyflowchart fizzbuzz_trace.py -o fizzbuzz_trace.html

# Step 4: Open the HTML File for Inspection
firefox fizzbuzz_trace.html
```

> [!WARNING]  
> Your (absolute/relative) path to the Python script may differ. If you need help with the setup, please come talk to me in the lab or drop by my office hours :)