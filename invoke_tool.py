# Import necessary libraries
import subprocess

# Define the tool
tool = 'summarizer-engine-v3'

# Invoke the tool and generate summary
try:
    result = subprocess.run([tool, "summary.txt"], stdout=subprocess.PIPE)
    print("Tool invoked successfully. Summary generated.")
except Exception as e:
    print(f"Failed to invoke tool: {str(e)}")

# Append the summary to README.md
try:
    import append_summary
    append_summary.append_summary()
    print("Summary appended to README.md successfully.")
except Exception as e:
    print(f"Failed to append summary to README.md: {str(e)}")