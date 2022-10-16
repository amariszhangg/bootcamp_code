"""
Programming Task #1
Given a list of digits, determine the integer that it represents.
For example, given the list: [8,3,5,1], your program should output 8351.
"""

def integer_assembler(int_list: list[int]):
    index = 0
    result = 0
    for num in range(len(int_list)-1, -1, -1):
        result += int_list[num] * 10**index
        index += 1

    return result

# example
print(integer_assembler([8,3,5,1]))
