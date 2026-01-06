# Description
The code provided implements a utility for computing the difference between two texts using the Longest Common Subsequence (LCS) algorithm. This utility is often used in version control systems and text comparison tools to highlight the changes made between two versions of a document or code file.

# Usage
To use the print_diff function:

Provide the paths to the two files you want to compare *(for example file1 and file2)* and call the print_diff function with the file paths as arguments.

Example usage:

```sh
file_1 = "file_1.txt"
file_2 = "file_2.txt"
print_diff(file_1, file_2)
```

# Note
Ensure that both input files (file1 and file2) are text files.
This implementation assumes that lines in the input files are the units of comparison. If you want to compare texts differently (e.g., by words), modifications to the code might be necessary.
