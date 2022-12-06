# task: 
"""
Find a character which is the same in the two half of one line. 
Then give it a value according to this rules: 
- Lowercase a-z = 1–26.
- Uppercase A-Z = 27–52.

- broader assignment: 
Each rucksack has two large compartments. All items of a given 
type are meant to go into exactly one of the two compartments. 
The Elf that did the packing failed to follow this rule for 
exactly one item type per rucksack.

The Elves have made a list of all of the items currently in 
each rucksack (your puzzle input), but they need your help 
finding the errors. Every item type is identified by a single 
lowercase or uppercase letter (that is, a and A refer to 
different types of items).

The list of items for each rucksack is given as characters all 
on a single line. A given rucksack always has the same number 
of items in each of its two compartments, so the first half of 
the characters represent items in the first compartment, while 
the second half of the characters represent items in the second 
compartment.

Input starts: 
lflZfgnSnlmmlgGfjGthQPtLNsQhvbHLLpSS
zrCVDVFMJTCTcCJMwCThWbtbpbWpPbtbHPLQssLsHP
rBFcrwFzFwwVDcDrzTzJfnRGjllBdGZnnZfhqmdn
 """ 
total_value = 0 

def halfs_of_line(number_of_char, line): 
    """Returns two halfs of one line. """
    first_half = 0
    second_half = 0
    half = int(number_of_char / 2)
    first_half = line[0:half]
    second_half = line[half:]
    print(first_half, len(first_half), second_half, len(second_half))
    return first_half, second_half

def find_the_same_letter(first_half, second_half): 
    """Returns the same character of two given strings. """
    for char in first_half: 
        if char in second_half: 
            print(char, end='\t')
            return char

def prioritize_char(char): 
    """Gives the char a value according to this rules: 
        - Lowercase a-z = 1–26.
        - Uppercase A-Z = 27–52."""
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if char in lowercase: 
        char_value = lowercase.index(char) + 1
        return char_value
    elif char in uppercase: 
        char_value = uppercase.index(char) + 27
        return char_value



with open('day03_input.txt') as file: 
    for line in file: 
        line = line.rstrip()
        print(len(line))
        number_of_char = len(line)
        first_half, second_half = (halfs_of_line(number_of_char, line))
        the_same_letter = find_the_same_letter(first_half, second_half)
        char_value = prioritize_char(the_same_letter)
        print(f'{char_value}')
        total_value += char_value
    print(total_value)