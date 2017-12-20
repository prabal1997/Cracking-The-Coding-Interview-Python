import sys
import random

#define a function for printing a grid
def print_grid(input_grid):
    print("||-------||");
    for row in input_grid:
        print(row);
    print("||-------||");

#input parameters
M, N = 5, 7;
max_val = 5;

#use hashtables as SETS (because insertion in hash-table is O(1), but for sets it is O(n))
row_hash_table = {};
col_hash_table = {};

#create a grid for testing purposes
grid = [ [random.randint(0, max_val) for col in range(N)] for row in range(M) ];
print_grid(grid);

#check the rows, cols that need to be set to zero (in O(MN))
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if (not grid[row][col]):
            row_hash_table[row] = True;
            col_hash_table[col] = True;
            
#go through elements in the hash-tables, clear the rows and the columns in (in O(MN))
for row in row_hash_table:
    grid[row] = [0] * len(grid[row]);

for col in col_hash_table:
    for row in range(len(grid)):
        grid[row][col] = 0;

#print the output
print_grid(grid);