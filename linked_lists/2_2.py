import sys
from node import node

#input params
input_list = [-1, 1, 3, 7, 11, 9, 2, 3, 5];
k_value = 3;

#convert list to linked-list
if (not input_list):
    print("ERROR: no list found.");
    exit(0);

head = node(input_list[0]);
current_ref = head;
for index in range(1, len(input_list)):
    current_ref.add_next(node(input_list[index]));
    current_ref = current_ref.next;
    
#print the k-th element from the end
head.print_list();
if (k_value > len(input_list)):
    print("FATAL ERROR:")

k_value = len(input_list-k_value);
current_ref = head;
for index in range(len(input_list)):
    if (index == k_value):
        print("OUTPUT: " + str(current_ref.value));
        break;
    else:
        current_ref = current_ref.next;