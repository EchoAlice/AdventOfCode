if __name__ == "__main__":
    
    #Read text file into numbers within an array
    with open("input.txt") as values:
        depths = values.readlines()

    previous_element = 0
    depth_increases = 0
    
    #Set up a for each loop
    for depth in depths:
        #compare the this character with the one in front of it
        depth_calculation = int(depth) - previous_element
        if depth_calculation > 0 and previous_element != 0:
            #decreasing from the previous element
            depth_increases += 1
        previous_element = int(depth)
    print(depth_increases)

    
