import sys

input_string = "art";

#ALGORITHM EXPLANATION: we go through each letter, put it into hashmap. If collision occurs, then repetitione existed.
#NOTE 1: this runs in O(n) time, assuming the hash-table provides an average rutime of O(1)
#NOTE 2: If you were to use the 'try'-'except' approach, know that the runtime would become O(n) because the hashtable would search for the object EVERYWHERE.
hashmap, sum_val= {}, 0;
expected_sum = len(input_string)*(len(input_string)+1)//2;

for index, letter in enumerate(input_string):
    hashmap[letter] = index+1;
    
for element in hashmap:
    sum_val += hashmap[element];

#note that the sum HAS to be strictly greater than the expected sum if repetition occurs
if (sum_val != expected_sum):
    print("REPEATITION EXISTS");
else:
    print("UNIQUE STRING");
