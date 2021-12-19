if __name__ == "__main__":
    
    #Read text file into numbers within an array
    with open("input_test.txt") as values:
        depths = values.readlines()
            
    previous_int = 0
    current_int = 0
    
    #Change depths to ints
    for i in range(len(depths)):
        current_int = int (depths[i] + depths[i + 1] + depths[i + 2])
        print(current_int)

        if i > 0:
            previous_int = int (depths[i - 1] + depths[i] + depths[i + 1])
            print(previous_int)
        
      
    



 # Day 1 part 1 code.  Useful info       
        
            
   #depth_calculation = int(depth) - previous_element
    #if depth_calculation > 0 and previous_element != 0:
        #decreasing from the previous element
    
    #depth_increases += 1
    #previous_element = int(depth)