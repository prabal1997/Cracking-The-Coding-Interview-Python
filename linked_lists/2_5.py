import sys
from node import *

#input params (NOTE: the first element of the list is the LEAST SIGNIFICANT)
input_num_1 = [2, 3];
input_num_2 = [1, 9 , 9, 3];

#make linked-lists
list_1 = node(); list_1.make_list(input_num_1);
list_2 = node(); list_2.make_list(input_num_2);

#add the numbers by iterating through them
if (len(input_num_1) < len(input_num_2)):
    #make sure that the first list is the LARGER one
    input_num_1, input_num_2 = input_num_2, input_num_1;
    list_1, list_2 = list_2, list_1;

#go through the lists, add them with the carried-over values
head = node(list_1.value + list_2.value);
iterator = head;

list_1_iterator = list_1.next;
list_2_iterator = list_2.next;

carry_over = 0;

for index in range(1, len(input_num_1)):
    #calculate raw sum of digits
    iterator.next = node(list_1_iterator.value + carry_over);
    if (index < len(input_num_2)):
        iterator.next.value += list_2_iterator.value 
    
    #separate the carry-over, and the newly calculated digit
    carry_over = iterator.next.value//10;
    iterator.next.value = (iterator.next.value)%10;
    
    #increment counter
    iterator = iterator.next;
    list_1_iterator = list_1_iterator.next;
    if (index < len(input_num_2)):
        list_2_iterator = list_2_iterator.next;

#print output
print("INPUTS: ");
list_1.print_list();
list_2.print_list();
print("SUM: ");
head.print_list();