import sys
from tree import binary_tree
from rand_node import random_travel
from random import randint

#input params (NOTE: we make a graph by mis-using(?) the binary-tree API)
input_list = [0, -100, 100, -50, 50, -25, 25, -75, 75, -37, 37, 73, 27, 69, -31, -88, -99];
tree = binary_tree(input_list);

#we get two random nodes from the tree using 4_11.py
random_measure = 7;
if ( not (0 <= random_measure < len(input_list)) ):
    print("ERROR: input out of range");
    exit(-1);

#we make a random graph given the initial binary tree
rand_nodes = [random_travel(tree) for index in range(random_measure)];
for node in rand_nodes:
    
    #choose a random node from the list
    rand_node = node;
    while(rand_node == node):
        rand_node = rand_nodes[randint(0, len(rand_nodes)-1)];
    
    #choose the left or the right subtree to modify
    choice = randint(0, 1);
    if (not choice):
        if (rand_node != node.next):
            node.prev = rand_node;
    else:
        if (rand_node != node.prev):
            node.next = rand_node;

#attempt printing the graph
print("OUR SEMI-RANDOM GRAPH: ");
for element in tree.ref_list:
    output = [None, str(element.value), None];

    #show the neighbours in the output
    if (element.prev):
        output[0] = element.prev.value;
    if (element.next):
        output[2] = element.next.value;
        
    #print the 'output' list as a string
    print(output);

#choose two RANDOM nodes from the graph to work with
rand_node_1, rand_node_2 = tree.ref_list[randint(0, len(tree.ref_list)-1)], tree.ref_list[randint(0, len(tree.ref_list)-1)];

print("");
print("RANDOM NODE 1: "+str(rand_node_1.value));
print("RANDOM NODE 2: "+str(rand_node_2.value));

#SOLUTION STARTS HERE:

#we use DFS to check if there's a path b/w two nodes
#NOTE: since we are working on a graph and NOT a tree, we NEED to have 'visited' fields to make sure our DFS works properly

for node in tree.ref_list:
    node.visited = False;

def backtrack(start_node, dest_node):
    #handle the case where there's no node in graph
    if (not start_node):
        return False;
        
    #check if we have a solution
    if (start_node == dest_node):
        return True;
    else:
        #mark this node visited
        start_node.visited = True;
        
        #make a list of candidates
        cand_list = [start_node.prev, start_node.next];
        cand_list = [element for element in cand_list if ( element and (not element.visited) )];
        
        #make a recursive call, and see if your neighbours can find a path
        output_bool = False;
        for element in cand_list:
            output_bool = backtrack(element, dest_node);
            if (output):
                return True;
        return False;

#call the DFS method, print results
output = backtrack(rand_node_1, rand_node_2);
print("PATH B/W NODES DOES" + ("" if output else " NOT") + " EXIST");