import sys
from rand_node import random_travel
from tree import binary_tree
from random import randint

#input params
input_list = [-3, -2, 1, 9, 5, -1, 11];
tree = binary_tree(input_list);

#NOTE: we find a random 'node' to make a sub-tree from OR we generate a random tree
rand_subtree = None;
rand_tree = None;
if (randint(0, 1)):
    rand_subtree = random_travel(tree);
else:
    rand_input_list = [randint(-10, 10) for index in range(len(input_list)//2)];
    rand_tree = binary_tree(rand_input_list);
    rand_subtree = random_travel(rand_tree);

#SOLUTION STARTS HERE

#we convert input tree to a 'string' using pre-order traversal that keeps track of parent-child relationship
#NOTE: this DOES NOT work with in-order traversal due to it simply sorting the tree contents
def pre_order(input_node, final_list):
    #handle special case
    if (not input_node):
        final_list.append(None);
    else:
        #append the current node and it's parent-child relation within the tree
        left_val, right_val = None, None;
        if (input_node.prev):
            left_val = input_node.prev.value;
        if (input_node.next):
            right_val = input_node.next.value;
        final_list.append((left_val, input_node.value, right_val));
        
        #traverse the children nodes
        pre_order(input_node.prev, final_list);
        pre_order(input_node.next, final_list);
          
#convert input list to traversal
input_trav_string = [];
pre_order(tree.root, input_trav_string);

test_trav_string = [];
pre_order(rand_subtree, test_trav_string);

string_list = [input_trav_string, test_trav_string];
string_list = [str(element)[1:-1] for element in string_list];

print("INPUT TREE: ", string_list[0]);
print("TEST  TREE: ", string_list[1]);

#NOTE: this sub-string search algorithm in python runs in average of O(M+N) and worst-case O(M*N);
if (string_list[1] in string_list[0]):
    print("\nMATCH FOUND!");
else:
    print("\nNO MATCH FOUND!");
