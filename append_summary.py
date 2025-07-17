import os

def append_summary():
    with open("README.md", "a") as readme_file:
        with open("summary.txt", "r") as summary_file:
            summary = summary_file.read()
            readme_file.write("\n" + summary)

if __name__ == "__main__":
    append_summary()