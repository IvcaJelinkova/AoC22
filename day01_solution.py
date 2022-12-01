# task: 
""" 
This list "day01_input" represents the Calories of the food carried by Elves:

The first Elf is carrying food with 4035, 10596, 17891, 5278 Calories, a total of 37800 Calories.
The second Elf is carrying food with 11293, 8478, 10874, 10582, 10756, 6649 Calories.
...
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: 
they'd like to know how many Calories are being carried by the Elf carrying the most Calories.

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?"""


def compare(the_biggest, new_number): 
    """Returns True if the_biggest is bigger or the same than new_number. 
    False otherwise. """
    if the_biggest <= new_number: 
        return True
    else: 
        print('staré je větší! :( ')
        return False



# loading the file with data:
elf = 1
elfs = {}
the_biggest = 0
the_strongest_elf = 1
second_strongest = 1
third_strongest = 1
sum = 0

# data preparation & giving data to sql:
with open('day01_input.txt', encoding='utf-8') as file:
    for line in file: 
    #str_data = file.read()
        line = line.rstrip()
        try: 
            if line[0].isdigit(): 
                line = int(line)
                if elf in elfs: 
                    sum_of_calories = elfs[elf] + line
                    elfs[elf] = sum_of_calories
                else: 
                    elfs[elf] = line
        except IndexError: 
            elf += 1
            continue
        else: 
            new_number = elfs[elf]
            if compare(the_biggest, new_number): 
                the_biggest = new_number
                the_strongest_elf = elf
                #print(f'New the biggest: {the_biggest}, {the_strongest_elf}')
    print(f'elfs: {elfs}, the biggest callories: {the_biggest}, the strongest elf: {the_strongest_elf}')
         
            
        
    

    """ 
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    if :
        print()
    
""" 
