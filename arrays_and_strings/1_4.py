import sys

input_string = "ljjojl";

#remove spaces from python string
input_string = (letter for letter in list(input_string) if not letter.isspace());
input_string = "".join(input_string);

#use hashtable to count letter frequency
hash_table = {};
for letter in input_string:
    if (letter in hash_table):
        hash_table[letter] += 1;
    else:
        hash_table[letter] = 1;

#check frequency of each letter
two_freq, one_freq = 0, 0;
for letter in hash_table:
    one_freq += (hash_table[letter]%2);
    two_freq += not (hash_table[letter]%2);

#give an output based on the count
if (one_freq <= 1):
    print("PALINDROME");
else:
    print("NOT PALINDROME");