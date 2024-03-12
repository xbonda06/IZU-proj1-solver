import difflib
import sys
import re


def read_file(filename):
    with open(filename, 'r') as file:
        return [re.sub(r'\s+', '', line).lower() for line in file]


def compare_files(file_path1, file_path2):
    content1 = read_file(file_path1)
    content2 = read_file(file_path2)

    d = difflib.Differ()
    diff = list(d.compare(content1, content2))

    has_differences = any(line.startswith(('-', '+')) for line in diff)

    if has_differences:
        print("Difference of two files:")
        for line in diff:
            if line.startswith('+ '):
                print(f"В {file_path2}: {line[2:]}")
            elif line.startswith('- '):
                print(f"В {file_path1}: {line[2:]}")
    else:
        print("Files are same.")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: script.py file1.txt file2.txt")
    else:
        file_path1 = sys.argv[1]
        file_path2 = sys.argv[2]
        compare_files(file_path1, file_path2)
