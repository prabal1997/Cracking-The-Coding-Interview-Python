import sys
from tree import binary_tree
from random import randint

#input params
input_list = [-3, -2, 1, 9, 5, -1, 11];
tree = binary_tree(input_list);

target_sum = -5;

#SOLUTION: perform a DFS (using backtracing) from EVERY node, and see if it adds up to a particular value
#NOTE 1: since there are NO loops in a tree, we DO NOT need to have a 'visited' node to check if a node's been visited already
#NOTE 2: since the values can be +ve/-ve, we NEED to continue searching the path we are on even after we've found one sum. Note the following example 0->(-1)->(1) which sums to value of '0' twice

def backtrack(input_node, input_sum, target, sum_ref):
    
    #handle the case when the root is empty
    if (not input_node):
        return;
    
    #check if you are a solution, and increment counter if 'true'
    #NOTE: despite having found one solution, we KEEP looking on the same path
    if (input_node.value + input_sum == target):
        sum_ref[0] += 1;

    #make a list of candidates
    cand_list = [input_node.prev, input_node.next];
    cand_list = [element for element in cand_list if element];
    
    #go through each candidate
    for element in cand_list:
        input_sum += input_node.value;
        backtrack(element, input_sum, target, sum_ref);
        input_sum -= input_node.value;

    return;
    
#perform backtracking starting from ALL nodes in the tree
new_list = [0];
for element in tree.ref_list:
    backtrack(element, 0, target_sum, new_list);

#print the output
print("WE HAVE FOLLOWING LEVELS IN OUR TREE:");
tree.print_tree();
print("");

print("TOTAL NUMBER OF WAYS: " + str(new_list[0]));