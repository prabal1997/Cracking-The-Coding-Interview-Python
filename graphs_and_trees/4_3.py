import sys
from tree import binary_tree

input_list = [1, -2, 9, -3, 5, -1, 11];
tree = binary_tree(input_list);

#print all the different levels of the tree
print("LIST OF ALL LEVELS:");
tree.print_tree();