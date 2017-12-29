import sys
import random
from tree import binary_tree

#input params
input_list = [-3, -2, 1, 9, 5, -1, 11];
tree = binary_tree(input_list);

print("LEVELS OF OUR TREE:");
tree.print_tree();
print("");

#find a random node
first_val = random.randint(0, len(input_list)-1);
second_val = first_val;
while (second_val == first_val):
    second_val = random.randint(0, len(input_list)-1);

#finding the nodes
node_1, node_2 = tree.search_tree(input_list[first_val]), tree.search_tree(input_list[second_val]);
print("FIRST  NODE: " + str(node_1.value));
print("SECOND NODE: " + str(node_2.value));

#finding common parent
def find_common(tree, node_1, node_2):
    #check if both nodes exist
    if ( (not tree.root) or (not node_1) or (not node_2) ):
        return None;
    
    #measure depth of each node
    first_len, second_len = tree.give_depth(node_1), tree.give_depth(node_2);
    
    #find the longer/shorter depth node
    sort_list = [[first_len, node_1], [second_len, node_2]];
    sort_list.sort(key=lambda element: element[0]);
    
    #traverse the extra length towards root, so that we start from the SAME depth from the root
    small, large = sort_list;
    extra_len = large[0]-small[0];
    while(extra_len):
        large[1] = large[1].parent;
        extra_len -= 1;
        
    #traverse upwards together, see if a collision happens
    while(small[1] != large[1]):
        small[1], large[1] = small[1].parent, large[1].parent;
        small[0] -= 1;
    return small[1];
    
#finding the common node
print( "THE LATEST COMMON ANCESTOR IS: " + str(find_common(tree, node_1, node_2).value) );