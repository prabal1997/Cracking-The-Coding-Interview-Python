import sys
import math

input_string = "";
test_string = "";

#creating a function to return 'error' values when strings are accessed out-of-range
if (abs(len(input_string)-len(test_string)) > 1):
    print(">1 EDITS!");
    exit(0);

RANGE_ERROR = -1;
give = lambda input_string, index: input_string[index] if ( 0 <= index < len(input_string) ) else RANGE_ERROR;

#we go through both strings in parallel, and perform the three operations if neccesary; we later check how many operations we performed in total
input_index, test_index = 0, 0;
edit_count = 0;

while(edit_count < 2):

    #checking if letters are identical
    input_s, test = give(input_string, input_index), give(test_string, test_index);

    #break if the strings have been completely scanned
    if (input_s == -1 or test == -1):
        edit_count += (input_s != test);
        break;

    #check if they are the same letter
    if (input_s == test):
        input_index += 1; test_index += 1;
        continue;

    #perform one of the possible actions if the letters are difference
    edit_count += 1;
    if (len(input_string) < len(test_string)):
        #we delete
        test_index += 1;
    elif (len(input_string) > len(test_string)):
        #we insert
        input_index += 1;
    else:
        #we match
        input_index += 1;
        test_index += 1;

#make output        
if (edit_count >= 2):
    print(">=2 EDIT COUNT");
if (edit_count == 1):
    print("1 EDIT COUNT");
if (edit_count == 0):
    print("NO EDITS REQUIRED");

        
            
        
