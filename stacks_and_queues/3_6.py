import sys
#NOTE: this is the previously designed linked-list node
sys.path.append('../linked_lists');
from node import *
import __builtin__

class animal:
    #NOTE: the two different types are DOG, CAT
    DOG, CAT = 0, 1;
    
    def __init__(self, animal_type=None):
        self.type = animal_type;
        
    def give_type(self):
        return ("DOG" if (self.type == self.DOG) else "CAT");
        
    def set_type(self, input_type):
        self.type = input_type if (input_type!=None) else None;
            
#input params: we make a list of animals
x = queue([animal(animal.CAT), animal(animal.DOG), animal(animal.DOG), animal(animal.CAT), animal(animal.DOG), animal(animal.CAT), animal(animal.CAT)]);

#SOLUTION:
x.print_queue();
x.extend([animal(animal.CAT)]);
x.deque_element();
x.print_queue();