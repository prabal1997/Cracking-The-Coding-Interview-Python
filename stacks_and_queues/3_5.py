import sys

#input params (i.e. stack to be sorted)
input_stack = [-1, 9, 2, 2, -7, 3, 0, 3, 7, 1, 8, 5, -4, 8];

#SOLUTION: repeatedly move stack b/w two stacks, hold the min. value in a var, push it to buffer - now only use the section of the buffer ABOVE the last 'min' value on the buffer
#NOTE: the solution runs in O(n^2) (amortized)
if (not input_stack):
    print("ERROR: empty input stack.");
    exit(0);

buffer_stack = [];
max_val = max(input_stack)+1;
size, counter, min_val, prev_val, freq = len(input_stack), 0, max_val, -float('inf'), {};

while(counter < size):
    while(input_stack):
        value = input_stack.pop();

        if (value not in freq):
            freq[value] = 1;
        else:
            freq[value] += 1;

        if ( (value < min_val) and (value > prev_val) ):
            min_val = value;

        buffer_stack.append(value);
    
    #move all the original elements back to the input list
    while(len(input_stack) < size):
        input_stack.append(buffer_stack.pop());
    
    #push the minimum value to the buffer
    freq_var = freq[min_val];
    counter += freq_var;
    while(freq_var):
        buffer_stack.append(min_val);
        freq_var -= 1;
    
    #reset parameters
    prev_val = min_val;
    min_val, freq = max_val, {};
    
#clear the input stack, move all buffer elements to it
input_stack = buffer_stack[::-1];

#print the list
print(input_stack);