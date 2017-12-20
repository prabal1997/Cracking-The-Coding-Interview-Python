import sys
from node import *

#input params
input_list = [-1, 1, 3, 7, 11, 9, 2, 3, 5];
partition = 5;

#make a linked-list using the input list
head = node(input_list[0]);
current_ref = head;
for index in range(1, len(input_list)):
    current_ref.add_next(node(input_list[index]));
    current_ref = current_ref.next;
head.print_list();

#find where the first 'partition' ends i.e. the element right before where the second partition starts
new_node = node(None);
new_node.add_next(head);

current_ref = new_node;
partition_start, partition_ref = -1, None;
for index in range(len(input_list)+1):
    if (current_ref.next):
        if ( (current_ref.next).value >= partition ):
            partition_start = index-1;
            partition_ref = current_ref;
            
            break;
        else:
            current_ref = current_ref.next;

#check if partitioning is even possible
if (not partition_ref):
    print("ERROR: Cannot Partition.");
    exit(0);
    
#go through the list in O(n) and move the smaller elements in the second partition...
#...to the left partition

prev_ref = partition_ref;
current_ref = partition_ref.next;
for index in range(partition_start+1, len(input_list)):
    #check if we need to swap nodes
    if (current_ref.value < partition):
        prev_ref.next = current_ref.next;
        current_ref.next = partition_ref.next;
        partition_ref.next = current_ref;
        
        partition_ref = partition_ref.next;
        current_ref = prev_ref.next;
        partition_start += 1;
    else:
        prev_ref = prev_ref.next;
        current_ref = current_ref.next;
        
#fix the head of the linked-list
head = new_node.next;
    
#print the output
head.print_list();