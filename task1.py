"""
Programming Task #1
Given a list of digits, determine the integer that it represents.
For example, given the list: [8,3,5,1], your program should output 8351.

HOW THE CODE WORKS: Imagine all integers in the list are of base 10. Beginning from the rightmost (last) element, assign it an imaginary index 0, in that it is 10^0, which equals 1 -- this is your 'ones' decimal place. Then the next element to the left of it is index 1 (10^1 = 10; 
tens' decimal place) and so on. When you multiply each integer by its respective index that is a power of 10 (integer * 10^index), then add each result together, you will produce the correct corresponding output.
"""

def integer_assembler(int_list: list[int]):  # feed a list of integers into the function
    index = 0  # index begins at 0, which is your 'ones' in the context of decimal places
    result = 0  # initialise the output to 0
    for num in range(len(int_list)-1, -1, -1):  # begin at the rightmost index; step down (left) by 1 with each iteration; 
        result += int_list[num] * 10**index
        index += 1

    return result

# example
print(integer_assembler([2,0,7]))
print(integer_assembler([8,3,5,1]))
print(integer_assembler([6,9,0,4,4]))

