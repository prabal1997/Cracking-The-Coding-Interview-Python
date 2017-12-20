import sys
import random

#define a function for printing a grid
def print_grid(input_grid):
    print("||-------||");
    for row in input_grid:
        print(row);
    print("||-------||");
    
#prepare a grid for testing
N = 5;
MAX_VAL = 1000;
grid = [ [random.randint(0, MAX_VAL) for col in range(N)] for row in range(N) ];

#print initial grid
print_grid(grid)

#rotate the grid (in-place) by individually rotation each element of each LAYER by 90 degrees (takes O(N^2))
layers = N//2+N%2;
for col in range(layers):
    for row in range((N-1)-col, col, -1):
        val_list = (grid[row][col], grid[col][(N-1)-row], grid[(N-1)-row][(N-1)-col], grid[(N-1)-col][(N-1)-col]);
        grid[col][(N-1)-row], grid[(N-1)-row][(N-1)-col], grid[(N-1)-col][(N-1)-col], grid[row][col] = val_list;

#print final grid
print_grid(grid);