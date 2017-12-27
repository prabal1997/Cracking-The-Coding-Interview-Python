import sys
sys.path.append('../linked_lists');
from node import *

class graph:
    
    def __init__(self, input_file, data_type=str):
        #initialize variables
        self.ref_list = [];
        
        #pass on the work to other functions
        self.read_file(input_file, data_type);
            
    def read_file(self, input_file, data_type=str):
        #basic error checking
        if (not isinstance(input_file, str)):
            print("ERROR: expected name of the configuration file not provided.");
            return;
        
        #read the file
        raw_input = list(open(input_file, "r"));
        raw_input = [(element.strip()).split(' ') for element in raw_input if (element.strip())[0]!='#'];
        self.ref_list = [0]*len(raw_input);
        
        for element in raw_input:
            #separating different parts of a node
            node_num = int(element[0]);
            node_val = data_type(element[1]);
            node_list = element[2:]; node_list = [int(element)-1 for element in node_list];
            
            #storing data in memory
            self.ref_list[node_num-1] = node(node_val);
            self.ref_list[node_num-1].next = node_list;

    def print_graph(self):
        print("||----||");
        for index, element in enumerate(self.ref_list):
            print(index, element.value, element.next);
        print("||----||");
    
    def __len__(self):
        return len(self.ref_list);
        
x = graph("source", float);
x.print_graph();