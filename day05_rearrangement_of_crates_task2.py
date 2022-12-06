# task: 
"""
After the rearrangement procedure completes, what crate ends 
up on top of each stack? 

There are crates in each stacks and they have to be rearrange
according to instructions below (p.e.: move 3 crates from stack
6 to stack 2. )

ONE DIFFERENCE FROM task1: Creates are moved all at a time. 
"""

import re

total_columns = 0
biggest_column = 0
total_rows = 0
first_column = []
second_column = []
third_column = []
fourth_column = []
fifth_column = []
sixth_column = []
seventh_column = []
eighth_column = []
ninth_column = []
instructions = []

def find_number_of_columns_and_rows(line):
    """Return number of columns in table. 
    Each row which interest us contains "[letter]", 
    one gap between squared bracket like "] [". 
    """ 
    columns = 0
    if "[" in line:
        row = 1
        for char in line: 
            if char == '[': 
                columns += 1
        return row, columns
    else: 
        return 0, 0

def load_input(biggest_column): 
    """Return lists of char for each column of the input table.
    We know number of rows and columns and indexes of each char. """
    number_of_index = biggest_column * 4 - 1
    input_columns = []
    with open('day05_input.txt') as f: 
        for line in f: 
            if '[' in line: 
                for i in range(1, number_of_index, 4):
                    if line[i] == ' ': 
                        pass
                    elif i == 1: 
                        first_column.append(line[i])
                    elif i == 5: 
                        second_column.append(line[i])
                    elif i == 9: 
                        third_column.append(line[i])
                    
                    elif i == 13: 
                        fourth_column.append(line[i])
                    elif i == 17: 
                        fifth_column.append(line[i])
                    elif i == 21: 
                        sixth_column.append(line[i])
                    elif i == 25: 
                        seventh_column.append(line[i])
                    elif i == 29: 
                        eighth_column.append(line[i])
                    elif i == 33: 
                        ninth_column.append(line[i])
                    
            elif 'move' in line: 
                instructions.append(unlock_instructions(line))
    print('Instructions: ', instructions)
    first_column.reverse()
    second_column.reverse()
    third_column.reverse()
    
    fourth_column.reverse()
    fifth_column.reverse()
    sixth_column.reverse()
    seventh_column.reverse()
    eighth_column.reverse()
    ninth_column.reverse()
    
    input_columns.append(first_column)
    input_columns.append(second_column)
    input_columns.append(third_column)
    
    input_columns.append(fourth_column)
    input_columns.append(fifth_column)
    input_columns.append(sixth_column)
    input_columns.append(seventh_column)
    input_columns.append(eighth_column)
    input_columns.append(ninth_column)
    
    return (first_column, second_column, third_column, input_columns, instructions)

def unlock_instructions(line): 
    """Instruction 'move 1 from 2 to 1' is given. This function return 
    3 numbers from this line in list [1, 2, 1]. """
    my_instruction = re.findall('[0-9]+', line)
    return my_instruction


def follow_instructions(input_columns, instructions): 
    """Follow given instructions on given columns. 
    Par example: 'move 1 from 2 to 1' = [1, 2, 1]
    This means remove last item from column 2 and put it into the last position 
    of column 1. """
    last_items = []

    for row in range(len(instructions)): # 1. řádek v délce 4
        print('instrukce: ', 'number=', instructions[row][0], 'from=', instructions[row][1], 'to=', instructions[row][2])
        number_of_items = int(instructions[row][0])
        from_column = int(instructions[row][1])
        to_column = int(instructions[row][2])
        selected_item = input_columns[from_column-1][-number_of_items:]
        print('selected item:', selected_item)
        del input_columns[from_column-1][-number_of_items:]
        input_columns[to_column-1] += selected_item
        print(input_columns, '\n')
    for i in range(len(input_columns)): 
        last_items.append(input_columns[i][-1])
    print('last: ', last_items)
    last_items = ''.join(last_items)
    print('last: ', last_items)     # NHWZCBNBF


with open('day05_input.txt') as file: 
    for line in file: 
        if line.startswith('move') == True: 
            pass
        else: 
            row, total_columns = find_number_of_columns_and_rows(line)
            total_rows = total_rows + row
            if total_columns > biggest_column: 
                biggest_column = total_columns
    print(f'Number of columns & rows: {biggest_column, total_rows}')
    first_column, second_column, third_column, input_columns, instructions = load_input(biggest_column)
    print(f'input column: {input_columns}')
    follow_instructions(input_columns, instructions)


