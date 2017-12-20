import sys

input_string_1 = "test";
input_string_2 = "tTtt";

#we make an assumption, and then try to disprove it
is_permutation = True;

#we hash the first string, then second string, and compare the frequency of letters in each
if (len(input_string_1) != len(input_string_2)):
    is_permutation = False;
else:
    #hash each string into a different table
    hash_table_1, hash_table_2 = {}, {};
    for input_string, hash_table in [(input_string_1, hash_table_1), (input_string_2, hash_table_2)]:
        for letter in input_string:
            if (letter in hash_table):
                hash_table[letter] += 1;
            else:
                hash_table[letter] = 1;

    #check if the hashed elements, and their values, are identical
    if (len(hash_table_1) != len(hash_table_2)):
        is_permutation = False;
    else:
        for letter in hash_table_1:
            if (letter in hash_table_2):
                if (hash_table_2[letter] != hash_table_1[letter]):
                    is_permutation = False;
            else:
                is_permutation = False;
                
            if (not is_permutation):
                break;

#print the message on the screen
if (is_permutation):
    print("STRINGS ARE PERMUTATIONS OF EACH OTHER");
else:
    print("STRINGS ARE NOT PERMUTATIONS OF EACH OTHER");
