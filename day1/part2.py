if __name__ == "__main__":
    
    #Read text file into numbers within an array
    # Change input_test.txt to input.txt!
    with open("input.txt") as values:
        depths = values.readlines()
    
    depth_increases = 0
    previous_int = 0
    current_int = 0
    number_of_inputs = len(depths)

    for i in range(number_of_inputs):
        if i < (number_of_inputs - 2):
            current_int = int(depths[i]) + int(depths[i + 1]) + int(depths[i + 2])
        if 0 < i < (number_of_inputs - 1):
            previous_int = int(depths[i - 1]) + int(depths[i]) + int(depths[i + 1])
        # Comparison Calculation
        if current_int > previous_int & previous_int > 0:
            depth_increases +=1
    print(depth_increases)