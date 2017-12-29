import sys
from tree import binary_tree

#input params
input_list = [-3, -2, 1, -2, 9, -3, 5, -1, 11];
tree = binary_tree(input_list);

starting_node = tree.root;

#find successor
print("ALL THE LEVELS OF THE TREE:");
tree.print_tree();

print("THE SUCCESSOR OF THE ROOT NODE IS " + str(tree.give_successor(starting_node).value) + ".");