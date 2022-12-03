# task: 
"""
Find a character which is the same in the three consecutive lines. 
Then give it a value according to this rules: 
- Lowercase a-z = 1–26.
- Uppercase A-Z = 27–52.

- broader assignment:  
The Elf that did the packing failed to follow this rule for 
exactly one item type per rucksack.

The Elves have made a list of all of the items currently in 
each rucksack (your puzzle input), but they need your help 
finding the errors. Every item type is identified by a single 
lowercase or uppercase letter (that is, a and A refer to 
different types of items).

The list of items for each rucksack is given as characters all 
on a single line. 
 """ 
total_value = 0 
three_consecutive_lines = 0
list_of_lines = []


def find_the_same_letter(list_of_lines): 
    """Returns the same character of three given strings. """
    print('list of lines: ', list_of_lines)
    for char in list_of_lines[0]: 
        if char in list_of_lines[1]: 
            if char in list_of_lines[2]: 
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
        three_consecutive_lines += 1
        if three_consecutive_lines < 4:
            list_of_lines.append(line)
        if three_consecutive_lines == 3:     
            the_same_letter = find_the_same_letter(list_of_lines)
            char_value = prioritize_char(the_same_letter)
            print(f'{char_value}')
            total_value += char_value
            three_consecutive_lines = 0
            list_of_lines = []
    print(total_value)