# IZU-proj1-solver
## solver.py
Script for solving the problem of finding the shortest path using the UCS algorithm (the version that uses the CLOSED list) and outputting each iteration of the algorithm in a user-friendly format. The script is written to solve the first project in the IZU course at VUT FIT in Brno.

To use the script, you need to define your own individual matrix, start point, and end point.

### Remark
Due to the specifics of matrices in Python, you should swap the x and y coordinates given in the assignment, as otherwise, it would require inverting the matrix provided to you, which is clearly more complex.
Despite this, the values are written out in the correct format.
### Usage
```bash
python3 solver.py
```
## compare.py
Additionally, a script named compare.py is included for comparing two files, in case you want to compare the solution provided by this solver with another solution. The script ignores newline characters, spaces, and uppercase.

### Usage
```bash
python3 compare.py file1 file2