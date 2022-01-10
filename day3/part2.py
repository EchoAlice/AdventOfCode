if __name__ == "__main__":
    # Read text file into numbers within 2 arrays
    with open("day3/input.txt") as values:
        o2_binary_input = values.readlines()
        co2_binary_input = o2_binary_input.copy()
        binary_input = [o2_binary_input, co2_binary_input]
    width = len(o2_binary_input[0]) - 1   
    binary_input_gamma = ""
    binary_input_epsilon = ""

# CO2 first, then O2.  I have my logic mixed up?
    answer = [0] * 2
    for i in range(len(binary_input)):
        print("i: " + str(i))
        # if binary_input[i] == ????
        for c in range(width):
            count_0 = 0
            count_1 = 0
            # Counts each bit in a column and records instances of each bit 
            for r in range(len(binary_input[i])):
                if int(binary_input[i][r][c]) == 0:
                    count_0 += 1
                if int(binary_input[i][r][c]) == 1:
                    count_1 += 1
           
            o2_remove_bit = 1 if count_0 > count_1 else 0
            co2_remove_bit = 0 if count_0 > count_1 else 1
            remove_bit = [o2_remove_bit, co2_remove_bit]

            removed = 0
            debug_count = 0
            # Removes number based on remove_bit 
            # When does list get messed up here?
            for r in range(len(binary_input[i])):
                debug_count = debug_count + 1
                if len(binary_input[i]) == 1:
                    answer[i] = binary_input[i]
                    break
                if int(binary_input[i][r - removed][c]) == remove_bit[i]: 
                    binary_input[i].remove(binary_input[i][r - removed])
                    removed = removed + 1
    # My program works with the test data, not with the final data.  answer[1] == 0 when using the real data.
    # Converts lists of one into strings
    a0 = answer[0]
    print("o2: " + str(a0))      # Why is o2 == 0?
    answer0 = ''.join(a0)
    a1 = answer[1]
    print("co2: " + str(a1))
    answer1 = ''.join(a1)

    co2_scrubber = int(answer0, 2)
    o2_generator =  int(answer1, 2)
    life_support = o2_generator * co2_scrubber
    print("Life support: " + str(life_support)) 