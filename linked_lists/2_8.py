import sys
from node import *

#input params
input_list_1 = list([1, 9, 3, 6, 5, 11, 3, 2]);

linked_list_1 = node();
linked_list_1.make_list(input_list_1);

index_to_loop = [5, 3];
linked_list_1.give_node(index_to_loop[0]).next = linked_list_1.give_node(index_to_loop[1]);

#solution: we use two poniters moving at different rates, and see if they ever meet
cycle_exists = False; #assume no cycle exists, try proving otherwise

iterator_1 = linked_list_1;
iterator_2 = linked_list_1;
start_test = False;
counter = 0;
while(iterator_1 and iterator_2):
    if (iterator_1 == iterator_2 and start_test):
        cycle_exists = True;
        break;
    start_test = True;    
    
    iterator_1 = iterator_1.next;
    iterator_2 = iterator_2.next;
    if (iterator_2):
        iterator_2 = iterator_2.next;
    
#print the output
if (cycle_exists):
    print("CYCLE EXISTS!");
else:
    print("NO CYCLE EXISTS!");