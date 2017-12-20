import sys

input_string = "aaaaaaaaaaaaaabca";

#compressing string
index = 1;
input_list = [ [input_string[0], 1] ];
while(index < len(input_string)):
    if (input_string[index] == input_string[index-1]):
        input_list[-1][1] += 1;
    else:
        input_list.append([input_string[index], 1]);
    index += 1;
    
new_string = ( (element[0]+str(element[1])) for element in input_list );
new_string = "".join(new_string);

#check if the compressed version is smaller or bigger than the original
if (len(input_string) <= len(new_string)):
    print(input_string);
else:
    print(new_string);
    