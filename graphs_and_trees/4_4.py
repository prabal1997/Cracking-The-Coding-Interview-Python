import sys
from tree import binary_tree

input_list = [-3, -2, 1, -2, 9, -3, 5, -1, 11];
tree = binary_tree(input_list);

#print all the different levels of the tree
print("LIST OF ALL LEVELS:");
tree.print_tree();

#check if the tree is balanced
def check_balanced(tree):
    #handle special case
    if (not tree.ref_list):
        print("ERROR: no tree found. Trivially balanced.");
        return True;
    
    def recurse(node):
        #check if we got an empty node
        if (not node):
            return (-1, True);
            
        left_height = recurse(node.prev);
        if (not left_height[1]):
            return (-1, False);
        right_height = recurse(node.next);
        if (not right_height[1]):
            return (-1, False);
        
        is_balanced = ( abs(left_height[0]-right_height[0]) <= 1 );
        return (1+max(left_height[0], right_height[0]), is_balanced);
        
    return recurse(tree.root)[1];

#check if the tree is balanced
print(check_balanced(tree));