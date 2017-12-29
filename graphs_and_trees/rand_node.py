import sys
from tree import binary_tree
from random import randint

#design a function that terminates at a random point on the graph
def random_travel(tree):
    #basic error checking
    if (not tree.root):
        return None;
        
    #measure the size-of sub-tree each node has
    def size_measure(input_node):
        #base case
        if (not input_node):
            return 0;
            
        #recursive calls
        left_size, right_size = size_measure(input_node.prev), size_measure(input_node.next);
        
        total_size = 1+left_size+right_size;
        input_node.total_size = total_size; #add a field to hold the 'total size' of a starting from that particular nod
        
        return(total_size);
        
    #store the size of sub-tree for EACH node...
    #...if it hasn't been done already
    total_size = 0;
    try:
        total_size = tree.root.total_size;
    except AttributeError:
        total_size = size_measure(tree.root);
     
    #handle the case when there's no data in the tree  
    if (not total_size):
        return None;
        
    #start traversing tree to find a random node in O(lg n)
    curr = tree.root;
    while(curr):
        #generate a range for random num
        total_range = curr.total_size;
        
        left_size = 0;
        if (curr.prev):
            left_size = curr.prev.total_size;
        right_size = 0;
        if (curr.next):
            right_size = curr.next.total_size;
        
        #generate random val., and choose a path of execution depending upon the val
        random_val = randint(1, total_range);

        if (1+1 <= random_val <= left_size+1):
            curr = curr.prev;
        elif(left_size+2<=random_val):
            curr = curr.next;
        else:
            break;
    
    #return the found node
    return curr;
        
            
    