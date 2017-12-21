import sys

class MyQueue:
    
    #initialize the main, buffer queues
    def __init__(self, input=[]):
        self.main_stack = [];
        self.buffer_stack = [];
        
        self.enqueue(input);
    
    #enqueue-ing a list of input data
    def enqueue(self, input_list):
        #very basic error checking
        if ( (input_list is None) ):
            print("ERROR: 'None' cannot be enqueued");
        if (not isinstance(input_list, list)):
            input_list = [input_list];
            
        #check if we need to move stuff to the main buffer
        if (self.buffer_stack):
            self.main_stack = self.buffer_stack[:];
            self.main_stack.reverse();
            self.buffer_stack = [];
            
        #add new elements to the queue
        self.main_stack.extend(input_list);
        
    def dequeue(self):
        #we try to save time by checking if the queue is already in the buffer
        if (len(self.buffer_stack) + len(self.main_stack)):
            if (self.buffer_stack):
                return self.buffer_stack.pop();
            else:
                self.buffer_stack = self.main_stack[:];
                self.buffer_stack.reverse();
                self.main_stack = [];
                return self.buffer_stack.pop();
        else:
            print("ERROR: attempted to dequeue an empty queue");
            
    def print_queue(self):
        print("FULL QUEUE: ");
        print("-> " + str(self.main_stack[::-1]+self.buffer_stack) + " ->");
        print("MAIN: ");
        print("-> "+str(self.main_stack[::-1])+" ->");
        print("BUFFER: ");
        print("-> "+str(self.buffer_stack)+" ->");
        print("");

#test-cases
x = MyQueue([1, 2, 3]);
x.print_queue();

x.dequeue();
x.print_queue();

x.dequeue();
x.print_queue();

x.dequeue();
x.print_queue();

x.enqueue([-1, 4, 3]);
x.print_queue();

x.dequeue();
x.print_queue();

x.enqueue(1);
x.print_queue();

x.enqueue(5);
x.print_queue();

x.dequeue();
x.print_queue();

x.dequeue();
x.print_queue();

x.dequeue();
x.print_queue();

x.dequeue();
x.print_queue();