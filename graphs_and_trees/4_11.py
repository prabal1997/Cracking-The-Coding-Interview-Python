#NOTE: this solution is in file 'rand_node.py'
from rand_node import random_travel
from tree import binary_tree

#input params
input_list = [-3, -2, 1, 9, 5, -1, 11];
tree = binary_tree(input_list);

#run a test
val_count = 15;
print(str(val_count) + " RANDOM VALUES FROM OUR TREE ARE:");
print([random_travel(tree).value for repeat in range(val_count)]);