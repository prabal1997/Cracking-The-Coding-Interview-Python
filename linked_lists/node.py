class node:
    def __init__(self, input_value=None):
        self.value = input_value;
        self.next = None;
        
    def add_next(self, input_node):
        self.next = input_node;
        
    def print_list(self):
        MAX_VAL = 10;
        output_list = [];
        
        #store data in a list
        current_ref = self;
        
        while(current_ref):
            output_list.append((current_ref.value, "->" if current_ref.next != None else None));
            current_ref = current_ref.next;
                
        #print, return data
        print(output_list);
        return output_list;
        
    def make_list(self, input_container):
        if (not input_container):
            print("ERROR: empty list given.");
            return;
        
        #make a linked-list using the container    
        current_ref = self;
        current_ref.value = input_container[0];
        for index in range(1, len(input_container)):
            current_ref.next = node(input_container[index]);
            current_ref = current_ref.next;
        
        return;
        
    def give_node(self, int_index):
        iterator = self;
        for index in range(int_index):
            iterator = iterator.next;
        return iterator;