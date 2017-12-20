import sys
from node import *

#input params
input_list = [-1, 1, 3, 7, 11, 9, 2, 3, 5];
delete_value = 3;

#make a linked list
if (len(input_list) <= 2):
    print("ERROR: list has nothing but the head and the tail.");

head = node(input_list[0]);
current_ref = head;
for index in range(1, len(input_list)):
    current_ref.add_next(node(input_list[index]));
    current_ref = current_ref.next;

head.print_list();

#NOTE: whichever node we delete CANNOT be the first of the last node
prev_ref = None;
current_ref = head;
for index in range(len(input_list)):
    if (0 < index < len(input_list)-1):
        if (current_ref.value == delete_value):
            prev_ref.next = current_ref.next;
            current_ref = prev_ref; #this leaves no reference to the deleted node
            break; #we break after having removed a single node
    
    #increment node
    prev_ref = current_ref;
    current_ref = current_ref.next;
    
head.print_list();