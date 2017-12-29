import sys
sys.path.append('../linked_lists');
from node import *
from collections import deque

#make a tree class
class binary_tree:
    
    def __init__(self, input_array=[]):
        #initialize tree
        self.root = None;
        self.count = 0;
        self.ref_list = [];
        
        #set tree attributes
        self.extend_tree(input_array);
    
    #searches for a value in the tree, returns the node
    def search_tree(self, input_value):
        #handling special case
        if (not self.root):
            return None;
            
        #searching for the value
        curr_ref, prev_ref = self.root, self.root;
        while(curr_ref and curr_ref.value != input_value):
            prev_ref = curr_ref;
            curr_ref = (curr_ref.prev if input_value <= curr_ref.value else curr_ref.next);
            
        if (not curr_ref):
            return None;
        else:
            return curr_ref;
    
    def give_depth(self, node):
        #handle special case
        if ( (not self.root) or (not node) ):
            return float('inf');
            
        #try finding node in tree
        curr, prev, counter = self.root, self.root, 0;
        while(curr and curr.value!=node.value):
            prev = curr;
            curr = (curr.prev if (node.value <= curr.value) else curr.next);
            counter += 1;
            
        if (not curr):
            return float('inf');
        else:
            return counter;
            
    def extend_tree(self, input_array):
        if (input_array):
            #convert received input to a list
            if (isinstance(input_array, str) or isinstance(input_array, tuple) or isinstance(input_array, set) or isinstance(input_array, dict)):
                input_array = list(input_array);
                
            #method to add each element to the tree
            def add_element(self, element):
                #increment counter
                self.count += 1;
                element = node(element);
                self.ref_list.append(element);
                
                #add the node to the tree
                if (not self.root):
                    self.root = element;
                else:
                    prev_ref, curr_ref = None, self.root;
                    while(curr_ref):
                        prev_ref = curr_ref;
                        if (element.value <= curr_ref.value):
                            curr_ref = curr_ref.prev;
                        else:
                            curr_ref = curr_ref.next;
                    #check where the new node fits
                    if (element.value <= prev_ref.value):
                        prev_ref.prev = element;
                    else:
                        prev_ref.next = element;
                    element.parent = prev_ref;
                
            #add each element to the tree
            for element in input_array:
                add_element(self, element);
    
    def give_height(self, input_node=None):
        #handling special case
        if (not input_node):
            input_node = self.root;
            
        #write a recursive function
        def height(input_node):
            if (not input_node):
                return (-1);
            else:
                return 1+max(height(input_node.prev), height(input_node.next));
                
        #return the output
        return height(input_node);
            
       
    def inorder_traversal(self):
        #repeatedly calling 'successors' to do an in-order walk
        output = [];    
        curr_ref = self.give_minimum();
        while(curr_ref):
            output.append(curr_ref);
            curr_ref = self.give_successor(curr_ref);
        
        #return of list of all the encountered nodes during the in-order walk
        return output;
            
        
    def give_minimum(self, input_node=None):
        #take care of the special case
        if (not input_node):
            input_node = self.root;
            
        #traverse as left as possible
        curr_ref = input_node;
        prev_ref = input_node;
        while(curr_ref):
            prev_ref = curr_ref;
            curr_ref = curr_ref.prev;
        
        #return the minimum node
        return prev_ref;
        
    def give_maximum(self, input_node=None):
        #special case
        if (not input_node):
            input_node = self.root;
        
        #traverse as right as possible
        prev_ref, curr_ref = input_node, input_node;
        while(curr_ref):
            prev_ref = curr_ref;
            curr_ref = curr_ref.next;
            
        #return the largest node
        return prev_ref;
    
    def give_successor(self, input_node):
        #basic error checking
        if (not input_node):
            return None;
    
        #find the successor
        if (input_node.next):
            #if a right-subtree exists, we return the left-most node in it
            prev_ref = input_node.next;
            next_node = prev_ref.prev;
            
            while(next_node):
                prev_ref = next_node;
                next_node = next_node.prev;
            
            return prev_ref;
        else:
            #if no right-subtree exists, we go to the parent...
            #we either return the parent, or the successor of the parent's parent;
            if (input_node.parent):
                if (input_node.parent.prev == input_node):
                    return input_node.parent;
                else:
                    current_ref = input_node.parent;
                    prev_ref = input_node;
                    while(current_ref and current_ref.next == prev_ref):
                        prev_ref = current_ref;
                        current_ref = current_ref.parent;
                    if (not current_ref):
                        return None;
                    else:
                        return current_ref;
            else:
                return None;
            
        
    #prints tree level-by-level
    def print_tree(self):
        print_list = [];
        queue = deque([self.root, None]);
        
        counter = self.give_height()+1;
        while(queue and counter):
            curr_ref = queue.popleft();
            
            #check if we have encountered another level
            if (not curr_ref):
                counter -= 1;
                
                print(print_list);
                print_list = [];
                queue.append(None);
                
                continue;
                
            new_elements = [curr_ref.prev, curr_ref.next];
            new_elements = [element for element in new_elements if element];
            queue.extend(new_elements);

            print_list.append(curr_ref.value);
    #this function returns 'False' if the value couldn't be removed, 'Yes' otherwise
    def delete_value(self, input_value):
        #handle the special case
        if (not self.root):
            return False;
        #find the element to be deleted
        curr, prev = self.root, self.root;
        while(curr and curr.value!=input_value):
            prev = curr;
            if (input_value <= curr.value):
                curr = curr.prev;
            else:
                curr = curr.next;
                
        #check the cause of termination
        if (not curr):
            return False;
        
        else:

            #check if the found node is the root, add a pseduo-node to simplify work
            is_root = False;
            if (curr == prev):
                is_root = True;
                prev = node(self.root.value-1);
                prev.next = self.root;

            #change the 'operating' node based on whether 'curr' <= 'prev' or not
            connect_node = None;
            if (prev.prev == curr):
                connect_node = -1;
            else:
                connect_node = 1;
                
            #re-attach the sub-trees of the removed node
            replacement_node = None;
            if (curr.next):
                min_node = self.give_minimum(curr.next);
                min_node.prev = curr.prev;
                
                replacement_node = curr.next;
                
            elif (curr.prev):
                max_node = self.give_maximum(curr.prev);
                max_node.next = curr.next;
                
                replacement_node = curr.prev;
                
            if (connect_node == -1):
                prev.prev = replacement_node;
            else:
                prev.next = replacement_node;
                
            #remove pseudo-node if the removed node was the roor
            if (is_root):
                self.root = prev.next;
            
            #remove the deleted node from the 'ref_list'
            #NOTE: this makes the algorithm O(n)
            idx = self.ref_list.index(curr);
            self.ref_list.pop(idx);
            
            self.count -= 1;
                            
            return True;
        
        
    def give_predecessor(self, input_node):
        if (not input_node):
            return None;
            
        #if we have a left-subtree, we return the maximum of it
        if (input_node.prev):
            return self.give_maximum(input_node.prev);
        else:
            #if we have no left-subtree, we check if we are the left-child of our parent
            if (input_node.parent and input_node.parent.next == input_node):
                return input_node.parent;
            else:
                #if we don't have a parent whose right child is us, we find the first ancestor whose right sub-tree contains us
                if (not input_node.parent):
                    return None;
                else:
                    curr_ref, prev_ref = input_node.parent, input_node;
                    while(curr_ref and curr_ref.prev == prev_ref):
                        prev_ref = curr_ref;
                        curr_ref = curr_ref.parent;
                    if (not curr_ref):
                        return None;
                    else:
                        return curr_ref;
                
            
#tree = binary_tree();
#tree.extend_tree([0, -1, 1, -3, -3, 3, 2, 5, 7]);
#tree.print_tree();
