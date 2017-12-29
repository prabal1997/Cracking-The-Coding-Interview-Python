import sys
from tree import binary_tree

input_list = [-3, -2, -1, 1, 5, 9, 11];
tree = binary_tree();

#make a recursive routine that vists the array elements in a 'binary search tree'-like method, and adds them to the actual tree...
#...while it does so
def minimal(array, range_arr, tree):
    #add the median to the tree
    median = sum(range_arr)//2;
    tree.extend_tree([array[median]]);
    
    #recursively add the array to the left and the right of the median
    left_range = [range_arr[0], median-1];
    if (left_range[1] >= left_range[0]):
        minimal(array, left_range, tree);
    right_range = [median+1, range_arr[1]];
    if (right_range[0] <= right_range[1]):
        minimal(array, right_range, tree);

#call the recursive routine    
if (not input_list):
    print("ERROR: no array");
    exit(-1);

minimal(input_list, [0, len(input_list)-1], tree);

#print the tree
print("LAYERS OF PRODUCED TREE:");
tree.print_tree();