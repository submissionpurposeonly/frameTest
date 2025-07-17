# Import necessary libraries
import subprocess

# Define the tool
tool = 'summarizer-engine-v3'

# Invoke the tool
try:
    result = subprocess.run([tool], stdout=subprocess.PIPE)
    print("Tool invoked successfully.")
except Exception as e:
    print(f"Failed to invoke tool: {str(e)}")