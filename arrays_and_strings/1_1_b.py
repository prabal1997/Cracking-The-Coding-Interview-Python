import sys

input_string = "test_me!";

#receive the word, sort the letters in a list, go through the list to check for repetitions
#NOTE: this runs in O(n*ln n) i.e. suitable for around 10M objects
input_list, not_unique = list(input_string), False;
input_list.sort();
for index, element in enumerate(input_list):
    if (input_list[index-1] == element):
        not_unique = True;
        break;

if (not_unique):
    print("NOT UNIQUE");
else:
    print("UNIQUE STRING");