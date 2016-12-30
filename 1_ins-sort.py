"""
function to demonstrate the insertion sort algorithm
input: list of integers
returns: list of integers (sorted)
"""
import random
import time

def sort_insertion(my_list):

    for i in range(1,len(my_list)):

        val_current = my_list[i]
        pos = i 
         
        # check backwards through sorted list for proper pos of val_current
        while((pos > 0) and (my_list[pos-1] > val_current)):
            my_list[pos] = my_list[pos-1]
            pos = pos-1
             
        if pos != i:
            my_list[pos] = val_current 
    
    return my_list 
    

if __name__ == "__main__":
    # Generate a list of random integers
    num_ints = 10
    my_list = random.sample(range(num_ints),num_ints)
    print "Unsorted list", my_list
    # Record start time
    t0 = time.clock()
    # Sort list
    sort_insertion(my_list)
    # Print elapsed time
    print "Sorted list" ,sort_insertion(my_list)
    print "Insertion Sort took: %s sec." %(time.clock() - t0)