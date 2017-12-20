import sys

#input parameters
input_string = "this is john smith      ";
actual_len = 18;

#SOLUTION:

#we start from the END because we have the buffer at the end, AND removing stuff from the back helps make more SPACE
input_string = list(input_string);

str_idx, wrd_idx = len(input_string)-1, actual_len-1;
while (str_idx >= 0 and wrd_idx >= 0):
    
    if (input_string[wrd_idx] == ' '):
        input_string[str_idx] = '0';
        input_string[str_idx-1] = '2';
        input_string[str_idx-2] = '%';
        str_idx -= 3;
    else:
        input_string[str_idx] = input_string[wrd_idx];
        str_idx -= 1;
    
    wrd_idx -= 1;    
    
print("".join(input_string));
    