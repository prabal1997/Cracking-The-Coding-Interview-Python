import sys
from tree import binary_tree

#input state
input_list = [-3, -2, 1, -2, 9, -3, 5, -1, 11];
tree = binary_tree(input_list);

#NOTE: the following (commented-out) code can be used to modify BSTs internal state to make it non-BST for testing purposes
'''
tree.root.value = 5;
my_node = tree.give_maximum();
my_node.value = tree.give_minimum().value;
'''

#check if the tree is balanced
def check_bst(tree):
    
    def start_check(node):
        #handle base case
        if (not node):
            return True;
            
        #check the left-subtree
        left_val = (-float('inf') if not node.prev else node.prev.value);
        left_bool = (False if left_val > node.value else start_check(node.prev));
        
        #check the right-subtree ONLY if the left one is valid
        if (left_val <= node.value and left_bool):
            right_val = (float('inf') if not node.next else node.next.value);
            right_bool = (False if right_val < node.value else start_check(node.next));
            
            return (right_bool and left_bool);
        else:
            return False;
            
    #call the recursive routine
    return start_check(tree.root);
    
#call the recursive routine to check whether our binary tree is also a binary search tree
print("LEVELS OF OUR TREE:");
tree.print_tree(); print("");

print("THE INPUT TREE IS" + (" NOT" if not check_bst(tree) else "") + " A BINARY TREE.");
