import sys
import math

class SetOfStacks:
    
    #define the size of EACH individual stack
    CHUNK = 7;
    
    def __init__(self, input_data=[]):
        self.size = 0;
        self.stack_count = 0;
        self.stack_stack = [];
        self.extend(input_data);
        
        #write data onto those stacks
        
    def extend(self, input_data):
        if (input_data == 13):
            print("FOUND");
            
        #re-format input argument as a list (UNLESS the input is 'None');
        if (input_data is None):
            print("ERROR: invalid input of 'None' type.");
        if (not isinstance(input_data, list)):
            input_data = [input_data];

        #record total length of the stack
        self.size += len(input_data);
        
        #check if the list exists
        rem_capacity = 0;
        if (self.stack_stack):
            rem_capacity = self.CHUNK - len(self.stack_stack[-1]);
            self.stack_stack[-1].extend(input_data[:min(len(input_data), rem_capacity)]);
        if (rem_capacity):
            input_data = input_data[min(len(input_data), rem_capacity):];
        
        #writing remaining stuff in additional stacks
        req_stacks = math.ceil(len(input_data)/self.CHUNK);
        if (req_stacks):
            self.stack_stack.extend([[] for index in range(req_stacks)]);
            for index in range(req_stacks):
                self.stack_stack[self.stack_count+index].extend(input_data[index*self.CHUNK: min((index+1)*self.CHUNK, len(input_data))]);
        
        #incrementing number of stacks in "SetOfStacks"
        self.stack_count += req_stacks;
            
    
    #prints the stack data onto console
    def print_stack(self):
        if (not self.size):
            print("ERROR: attempted to print an empty stack");
        for index, element in enumerate(self.stack_stack):
            print("STACK " + str(index) + ": ", element);
    
    #pop-off elements from the stack
    def pop(self, index=-1):
        if (self.size and (-1 <= index < self.stack_count) and self.stack_stack[index]):
            stack_object = self.stack_stack[index];
            
            output = stack_object.pop();
            if (not stack_object):
                self.stack_stack.pop(index);
                self.stack_count -= 1;
                
            self.size -= 1;
            
            return output;
        else:
            print("ERROR: attempted to pop an empty stack");
    
    def popAt(self, index):
        return self.pop(index);
        
#test-cases
x = SetOfStacks([-1, 3]);
x.print_stack();
print(x.size);
for index in range(22):
    x.extend(index);
x.print_stack();
for index in range(24):
    x.pop(0);
    x.print_stack();
    

