import sys
import itertools
from tree import binary_tree
from collections import deque

#input params
input_list = [-3, -2, 1, 9, 5, -1, 11];
#input_list = [2, 1, 3];
tree = binary_tree(input_list);

print("LEVELS OF OUR TREE:");
tree.print_tree();
print("");

'''
SOLUTION: note that -
*everything on the same level can be added in ANY ORDER
*every level should be added in ASCENDING ORDER
'''

#make a list of nodes on same level using BFS
node_list = deque([tree.root, None]);
counter = tree.give_height()+1;

final_list = [];
print_list = [];

while(counter and tree.root and node_list):
    element = node_list.popleft();
    if (not element):
        final_list.append(print_list);
        print_list = [];
        
        node_list.append(None);
        counter -= 1;
        
        continue;
        
    print_list.append(element.value);
    
    add_list = [element.prev, element.next];
    add_list = [element for element in add_list if element];
    
    node_list.extend(add_list);

#create all possible permutations at each level
final_list = [ list(itertools.permutations(element)) for element in final_list ];

#use backtracking to print all possibilities (NOTE: for efficiency, you can use a dynamically created for-loop)
def backtrack(input_list):
    
    #check if we have a solution at hand
    if (len(input_list) == len(final_list)):
        #re-format the list
        output = [];
        for storage in input_list:
            for element in storage:
                output.append(element);
        
        #print the formatted list
        print(output);
    else:
        #prepare a list of candidates
        candidates = final_list[len(input_list)];
        for element in candidates:
            input_list.append(element);
            backtrack(input_list);
            input_list.pop();

#execute the backtracking method
print("ALL THE POSSIBILITES ARE: ");
backtrack([]);

