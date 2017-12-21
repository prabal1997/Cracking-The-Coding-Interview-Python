import sys

#we make a class that can perform the operations described in 3.1 in O(1) (amortized) time
class stack:
    def __init__(self, input_container=[]):
        #maintain a stack of data, and a stack of MINIMUM values
        self.stack = [];
        self.min_stack = [];
        for element in input_container:
            self.push(element);
    
    def pop(self):
        #pop the stack, and see if the value popped is a part of the stack of minimum values
        output = self.stack.pop();
        if (self.min_stack and output == self.min_stack[-1]):
            self.min_stack.pop();
        return output;
        
    def push(self, input_data):
        #push element onto stack
        self.stack.append(input_data);
        #check if the new element's smaller than the global min. value
        if ( (not self.min_stack) or input_data <= self.min_stack[-1] ):
            self.min_stack.append(input_data);
            
    def peek(self):
        return self.stack[-1];
        
    def min(self):
        return self.min_stack[0];

    def print_stack(self):
        print("STACK: ");
        print(self.stack);
        print("MINIMUM VALUE STACK: ");
        print(self.min_stack);
        print("");
    
    def __len__(self):
        return len(self.stack);
    
    def __print__(self):
        print("MANGO!");

#example test-case
x, counter = stack([3, 9, 4, -1, 2, 5, -1, 3]), 0;
for value in range(len(x)):
    x.pop();
    if (counter%2):
        x.push(-counter);
    x.print_stack();
    print(x.peek());
    counter += 1;
