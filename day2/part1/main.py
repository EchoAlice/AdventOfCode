if __name__ == "__main__":
    
    # Read text file into numbers within an array
    with open("input.txt") as values:
        depths = values.readlines()

    # Iterate through all directional inputs
    horizontal_position = 0
    sub_depth = 0
    for depth in depths:
        # Splits each list object into seperate objects 
        direction = depth.split()      

        # Takes value and adds or subracts based on the direction
        if direction[0] == "forward":
            horizontal_position += int (direction[1])   
        if direction[0] == "up":         
            sub_depth -= int (direction[1])
        if direction[0] == "down":
            sub_depth += int (direction[1])

    answer = horizontal_position * sub_depth
    print(answer)
