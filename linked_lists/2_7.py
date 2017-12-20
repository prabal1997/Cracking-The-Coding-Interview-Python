import sys
from node import *

#input params, where we make two lists, and make them intersect
input_list_1 = list([1, 9, 3, 6, 5, 11, 3, 2]);
input_list_2 = list([11, -1, 2, 4, 3, 7, 8, 9]);
intersect_index = 3;

linked_list_1 = node();
linked_list_1.make_list(input_list_1);
linked_list_2 = node();
linked_list_2.make_list(input_list_2);

iterator_1 = linked_list_1;
for index in range(intersect_index):
    iterator_1 = iterator_1.next;
iterator_2 = linked_list_2;
for index in range(len(input_list_2)-1):
    iterator_2 = iterator_2.next;

iterator_2.next = iterator_1;

#we now inspect the two linked lists to see if they intersect...
#...by trying to see where two iterators (one for each list) itersect
print("FIRST LIST: ");
linked_list_1.print_list();
print("SECOND LIST: ");
linked_list_2.print_list();

iterator_1 = linked_list_1;
list_1_len = 0;
while(iterator_1):
    list_1_len += 1;
    iterator_1 = iterator_1.next;
    
iterator_2 = linked_list_2;
list_2_len = 0;
while(iterator_2):
    list_2_len += 1;
    iterator_2 = iterator_2.next;

#make sure that the first list is the larger one
if (list_1_len < list_2_len):
    list_1_len, list_2_len = list_2_len, list_1_len;
    linked_list_1, linked_list_2 = linked_list_2, linked_list_1;

#advance the iterator of first list so that iterator_1, iterator_2 have to cover the same total distance
advance_iterator_1 = list_1_len-list_2_len;
iterator_1, iterator_2 = linked_list_1, linked_list_2;
for index in range(advance_iterator_1):
    iterator_1 = iterator_1.next;

#we assume that the lists don't intersect, then we try to disprove it
does_intersect = False;
for index in range(list_2_len):
    if (id(iterator_1) == id(iterator_2)):
        does_intersect = True;
        break;
        
    iterator_1 = iterator_1.next;
    iterator_2 = iterator_2.next;
    
#print output
if (does_intersect):
    print("INTERSECTION HAPPENS!");
else:
    print("NO INTERSECTION HAPPENS!");