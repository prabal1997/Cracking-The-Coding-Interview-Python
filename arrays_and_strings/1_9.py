import sys

#input parameters
input_string = "mango";
test_string = "goman";

#SOLUTION: This is an O(n) solution on AVERAGE (where 'n' is the length of the LONGER string)
copy_string = 2*test_string;
if ( (input_string in copy_string) and (len(input_string)==len(test_string)) ):
    print("ROTATION DETECTED!");