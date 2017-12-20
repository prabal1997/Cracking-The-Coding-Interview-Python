import sys
from node import *

#input params
input_list = list("testtset");

#make a linked_list
if (not input_list):
    print("ERROR: No list found.");
    exit(0);
    
linked_list = node();
linked_list.make_list(input_list);

print("INPUT: ");
linked_list.print_list();

#check if the list is a palindrome by building a request stack, and then unrolling it
#NOTE: we use recursion because WE DO NOT KNOW THE TYPE OF ELEMENTS THE LIST MAY HAVE
stack = [[len(input_list), linked_list]];

build_stack = True;
while(build_stack):
    req = stack[-1];
    if (req[0] <= 1):
        build_stack = False;
        continue;
    else:
        new_req = [req[0]-2, req[1].next];
        stack.append(new_req);

last_element = None;
is_palindrome = True; #we ASSUME that the string is a palindrome, and try to disprove it
while(stack and is_palindrome):
    req = stack.pop();
    if (req[0] <= 1):
        if (req[0] == 1):
            last_element = req[1].next;
        if (req[0] == 0):
            last_element = req[1];
    else:
        if (last_element.value != req[1].value):
            is_palindrome = False;
            continue;
        else:
            last_element = last_element.next;

#print the verdict            
print(is_palindrome);