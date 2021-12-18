if __name__ == "__main__":
    
    #Read text file into numbers within an array
    with open("input_test.txt") as values:
        depths = values.readlines()

    previous_element = 0
    depth_increases = 0

    current_array = []*4
    next_array = []*4

    # Cycles through every value in input.txt
    for depth in depths:
        # How do I get depths to cycle through four elements, instead of copying the same one over and over        
        for i in range(4):
            if i < 3:
                # I want to print out value at depth + i
                print(depths[i])
                print(depths[i+1])
                print(depths[i+2])
                #current_array[i] = int (depth)
                #print("Current array: " + current_array[i])
            if i > 0:
                print(depths[i])
                print(depths[i+1])
                print(depths[i+2])
                #next_array[i] = int (depth)
                #print("Next array: " + str(next_array[i]))


    # At end of cycle, turn current array to previous array and rerun the loop.   Recursion???
            

        
        
        
        
            
   # depth_calculation = int(depth) - previous_element
    #if depth_calculation > 0 and previous_element != 0:
        #decreasing from the previous element
    
    #depth_increases += 1
    #previous_element = int(depth)