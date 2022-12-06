# task: 
""" 
This list "day01_input" represents the Calories of the food carried by Elves:

The first Elf is carrying food with 4035, 10596, 17891, 5278 Calories, a total of 37800 Calories.
The second Elf is carrying food with 11293, 8478, 10874, 10582, 10756, 6649 Calories.
...
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: 
they'd like to know how many Calories are being carried by the Elf carrying the most Calories.

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

Input starts: 
4035
10596
17891
5278

11293
8478
10874
10582
10756
6649

9707
""" 

# loading the file with data:
elf = 1
elfs = {}
the_biggest_calories = 0
the_strongest_elf = 1
sum = 0
helper = 0

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
          
    print(f'elfs: {elfs}\n\n')
    sorted_calories = sorted(elfs.values(), reverse=True)
    sorted_elfs = {}

    for i in sorted_calories: 
        for k in elfs.keys(): 
            if elfs[k] == i: 
                sorted_elfs[k] = elfs[k]
    print(sorted_elfs)

    for elf, calories in sorted_elfs.items(): 
        if helper < 3: 
            sum += calories
        else: 
            break
        helper += 1
        
    print('\nSum of three the best elfs: ', sum)


    
        