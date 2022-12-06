# task: 
""" 
In how many lines is one range occupied in the other? 
Every section has a unique ID number, and each Elf is assigned 
a range of section IDs.

Input starts: 
8-82,3-96
13-95,99-99

"""
import re
total_contain = 0


def number_selection(line): 
    """It select four number from one line. And add the numbers 
    between. 
    Par example: I have 2-4,6-8 and it return: 2, 4, 6, 8. """
    my_numbers = re.findall('[0-9]+', line)
    first_pair_start = int(my_numbers[0])
    first_pair_finish = int(my_numbers[1])
    second_pair_start = int(my_numbers[2])
    second_pair_finish = int(my_numbers[3])
    return first_pair_start, first_pair_finish, second_pair_start, second_pair_finish


def number_range(first_pair_start, first_pair_finish, second_pair_start, second_pair_finish): 
    """It return range of two pairs of number. 
    Par example: I have input 2, 4,6, 8 and it return: 
    first_range = 2, 3, 4
    second_range = 6, 7, 8. """
    first_range = []
    second_range = []
    for i in range(first_pair_start, first_pair_finish+1): 
        i = str(i)
        first_range.append(i)
    for i in range(second_pair_start, second_pair_finish+1): 
        i = str(i)
        second_range.append(i)
    first_range = ''.join(first_range)
    second_range = ''.join(second_range)
    print('first_range: ', first_range, end='\t')
    print('second range: ', second_range)
    return first_range, second_range


def contains_numbers(first_range, second_range): 
    """It return True if first pair of numbers is contains
    in the second or vice versa. Otherwise return False. """
    if first_range in second_range: 
        print('ano, první obsahuje druhý', end=' = ') 
        return True
    elif second_range in first_range: 
        print('ano, druhý obsahuje první', end=' = ')
        return True
    else: 
        return False
     

with open('day04_input.txt') as file: 
    for line in file: 
        line = line.rstrip()
        print(line)
        first_pair_start, first_pair_finish, second_pair_start, second_pair_finish = number_selection(line)
        first_range, second_range = number_range(first_pair_start, first_pair_finish, second_pair_start, second_pair_finish)
        contain = contains_numbers(first_range, second_range)
        if contain: 
            print('ano, obsahuje')
            if first_pair_start >= second_pair_start and first_pair_finish <= second_pair_finish: 
                print('jsem tu!! a vzyšuju', end='\t')    
                total_contain += 1
                print('subtotal: ', total_contain)
            elif second_pair_start >= first_pair_start and second_pair_finish <= first_pair_finish: 
                print('JSEM TU!! a vzyšuju', end='\t')    
                total_contain += 1
                print('subtotal: ', total_contain)
        print()
    print('TOTAL:', total_contain)


#není 616 ani 586 (too high)