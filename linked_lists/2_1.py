import sys
from node import *
 
#input parameters
input_list = [-1, 1, 3, 11, 2, -1, 3, 13, 0, 1];

#convert input to a linked list
if (not input_list):
    print("ERROR: no list found.");
    exit(0);

head = node(input_list[0]);
current_ref = head;
for index in range(1, len(input_list)):
    current_ref.next = node(input_list[index]);
    current_ref = current_ref.next;
    
#print the list
print("ORIGINAL LIST: ");
head.print_list();

#go through list to hash duplicates ONLY
hash_table = {};

current_ref = head;
for index in range(0, len(input_list)):
    if(current_ref.value in hash_table):
        hash_table[current_ref.value].append(index);
    else:
        hash_table[current_ref.value] = [];

    #increment node
    current_ref = current_ref.next;

#make a list of nodes to be removed, sort it in non-decreasing manner O(n*log(n))
remove_nodes = [];
for element in hash_table:
    remove_nodes.extend(hash_table[element]);
remove_nodes.sort();

#go through the linked-list while deleted elements
prev_ref, current_ref, index, list_index = None, head, 0, 0;
while(index < len(input_list) and list_index < len(remove_nodes)):

    #check if the node needs to be removed
    if (index == remove_nodes[list_index]):
        #remove current node
        prev_ref.next = current_ref.next;
        current_ref.next = None;
        
        #set new value for 'current_ref'
        current_ref = prev_ref.next;
        list_index += 1;
    else:
        prev_ref = current_ref;
        current_ref = current_ref.next;
    #increment counter
    index += 1;
         
#print list again
print("REDUCED LIST: ");
head.print_list();