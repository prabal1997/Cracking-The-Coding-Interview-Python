import sys

#input params (NOTE: we assume that the input-string is ALWAYS in a valid format)
input_string = "0&0&0&1^1|0";
desired_output = True;

#SOLUTION: use backtracking, where number of candidates depend upon the total number of operators being used

#counting operators
op_count = sum((True for char in input_string if char not in ('0', '1')));

print("INPUT: " + input_string);
#backtracking routine
def eval_count(og_string, result):
    #special case
    if (not og_string):
        return 0;
      
    #support routines for the 'backtracking' function
    def merge_table(val_table, val):
        for element in val:
            val_table[element] += val[element];
        return val_table;
    
    def give_table(operator, left_val, right_val):
        #count different types of possible pairs
        T_pairs, F_pairs = left_val[True]*right_val[True], left_val[False]*right_val[False];
        TF_pairs =  left_val[True]*right_val[False] + left_val[False]*right_val[True];

        #check which operator needs to be used
        val_func = None;
        if (operator is "^"):
            val_func = lambda x, y: x^y;
        elif (operator is "|"):
            val_func = lambda x, y: x|y;
        else:
            val_func = lambda x, y: x&y;
        
        #calculate true/false counts
        out_table = {False: 0, True: 0};
        
        out_table[val_func(1, 0)] += TF_pairs;
        out_table[val_func(1, 1)] += T_pairs;
        out_table[val_func(0, 0)] += F_pairs;
        
        #return the table
        return out_table;
        
    #backtracking routine  
    def backtrack(og_string, result, input_string, level=0):
        #check if you have the solution OR the base case
        if (not input_string):
            return 0;
        if (len(input_string) == 1):
            #print( "LEVEL " + str(level) + ": " + str(input_string) + " " + input_string );
            inp_val = bool(int(input_string));
            return {inp_val: 1, (not inp_val): 0};
        
        #prepare a list of candidates
        op_list = [(op, input_string[:idx], input_string[idx+1:]) for idx, op in enumerate(input_string) if op not in ('0', '1')];

        
        #make a table to hold number of true, false values
        val_table = {False: 0, True: 0};
        for cand in op_list:
            #calculate values of left, right sides
            left_val = backtrack(og_string, result, cand[1], level+1);
            right_val = backtrack(og_string, result, cand[2], level+1);
            
            #calculate the output table
            val = give_table(cand[0], left_val, right_val);
            val_table = merge_table(val_table, val);
        
        #return output
        if (og_string is input_string):
            return val_table[result];
        else:
            return val_table;
            
    #make recursive backtracking call
    return backtrack(og_string, result, og_string);
    
#make the call to 'eval_count' function
print("POSSIBLE SOLUTIONS: " + str(eval_count(input_string, desired_output)));