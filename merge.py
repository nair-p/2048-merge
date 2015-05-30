"""
 The program consists of a function merge that is used to merge similar elements in a list, used in the game 2048.

"""

def merge(original_list): 
    """
    Function that adds the 2 similar elements in a list for the game 2048
   
    """
    temporary_list = []
    final_list = []
    
# loop that adds all non - zero elements of the original list into a temporary list	
    for element in original_list:
        if element != 0:
            temporary_list.append(element)
            
# filling rest of slots of temporary list with 0s			
    while len(temporary_list) < len(original_list): 
        temporary_list.append(0)
    
    count_var = 0 # a temporary counter 
    flag_var = 0 #flag variable to check if there is change in input list
    
# if the list has even number of elements, add a 0
    if len(temporary_list)%2 == 0:
        temporary_list.append(0)

# traversing the list from the left
    while count_var < len(temporary_list) - 1:
        if temporary_list[count_var] == temporary_list[count_var + 1] and temporary_list[count_var]!=0:
            add =  2 * temporary_list[count_var]
            final_list.append(add)
            count_var = count_var + 2
        else:
            flag_var = flag_var + 1 #updating to see if no adding took place,  only shifting. 
            final_list.append(temporary_list[count_var])
            count_var = count_var + 1
    if count_var < len(temporary_list):
		# if there are any unadded non-zero elements in the list 
		final_list.append(temporary_list[count_var])
    
# adding the extra 0s at the end of the final list
    final_count = len(final_list)
    original_count = len(original_list)

    while final_count < original_count:
        final_list.append(0)
        final_count = final_count + 1
        
#printing the final list
    if flag_var == len(original_list):
        temporary_list.pop()
        return temporary_list
    else:
        return final_list
    
    
INPUT_LIST = [4,2,2]
OUTPUT_LIST = merge(INPUT_LIST)
print OUTPUT_LIST
